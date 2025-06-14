import pygame as pg
import pygame_gui as pgui

class Tile():
    """Basic tile class."""
    def __init__(self, pos:tuple = (0,0), pospx:tuple = (0,0), dim:tuple = (10,10), color:str = "black", state = None):
        """Constructor"""
        self._pos = pos
        self._pospx = pospx
        self._dim = dim
        self._color = color
        self._state = state
    

    def draw(self, win):
        """Class funciton to draw cell on window."""
        pg.draw.rect(win, self._color, (*self._pospx, *self._dim))


    def setState(self, state):
        """Update cell state."""
        self._state = state

    def setColor(self, color):
        """Updates color of cell."""
        self._color = color


class TileGrid():
    """Vidsial tile grid with pygame."""
    basicMod = {
        'winSize':(1000,500),
        'nx':10,
        'ny':5,
        'winPadding':5,
        'cellPadding':1,
        'FPS':30,
        'BGColor':(65,65,65),
        'cellColor':"white",
        'defaultCellState':None,
        'forceSqaure':False
    } # winSize, nx, ny, pad, cellPad, FPS, BGColor, cellColor, defaultCellState, square = self._mod.values()  # MODSIGNATURE
    
    basicUI = {
        'UIPlace':"left",
        'UISpace':200,
        'UIColor':"darkGray",
        'UIPos':None, # gets updated during initialization
        'UISize':None, # gets updated during initialization
    } # UIPlace, UISpace, UIColor, UIPos, UISize = self._UI.values() # UISIGNATURE

    
    def __init__(self, mod = None, fillTiles = True, action = None, UI = None, **kwargs):
        """Constructor"""
        pg.init()
        self._tiles = []
        self._objects = [] # objects goes here
        self._action = action # game goes here
        self._text = []

        if mod is not None:
            self._mod = mod
        else:  
            self._mod = TileGrid.basicMod

        for key, value in kwargs.items():
            if self._mod.__contains__(key):
                self._mod[key] = value
            elif (UI is None) and (TileGrid.basicUI.__contains__(key)):
                UI = 'auto'
        
        self._win = pg.display.set_mode(self._mod['winSize'])  
        self._manager = pgui.UIManager(self._mod['winSize'])
  
        if UI is not None:
            if UI == "auto":
                self._UI = TileGrid.basicUI
            self._buttons = {}
            self._textBoxes = {}

        else:
            self._UI = self._UI = {}
        
        for key, value in kwargs.items():
            if self._UI.__contains__(key):
                    self._UI[key] = value

        if (fillTiles):
            self.fillTiles(Tile)
        

    def fillTiles(self, CellType:type = Tile):
        """Fills inn board with grid tiles of spesific type."""

        winSize, nx, ny, pad, cellPad, _, _, cellColor, defaultCellState, square = self._mod.values() # MODSIGNATURE
        UIPad = [
            [0,0],  # left, right
            [0,0]   # top, bottom
        ]

        if self._UI:
            UIPlace, UISpace,  _, _, _ = self._UI.values() # UISIGNATURE

            if UIPlace in ['left', 'right']:
                self._UI['UISize'] = (UISpace, winSize[1])
                if UIPlace == 'left':
                    UIPad[0][0] = UISpace
                    self._UI['UIPos'] = (0,0)
                else:
                    UIPad[0][1] = UISpace
                    self._UI['UIPos'] = (winSize[0]-UISpace,0)

            elif UIPlace in ['top', 'bottom']:
                self._UI['UISize'] = (winSize[0], UISpace)
                if UIPlace == 'top':
                    UIPad[1][0] = UISpace
                    self._UI['UIPos'] = (0,0)
                else:
                    UIPad[1][1] = UISpace
                    self._UI['UIPos'] = (0,winSize[1]-UISpace)
        
        width, height = winSize
        width -= sum(UIPad[0])
        height -= sum(UIPad[1])

        cellWidth = (width-2*pad-(nx-1)*cellPad)/nx
        cellHeight = (height-2*pad-(ny-1)*cellPad)/ny

        if square:
            cellWidth, cellHeight = min(cellWidth, cellHeight), min(cellWidth, cellHeight)
        
        spaceX = cellWidth+cellPad
        spaceY = cellHeight+cellPad

        for x in range(nx):
            extendX = int((spaceX)*(x+1)) - int((spaceX)*(x)) - int(spaceX) # ensures even spacing between tiles

            for y in range(ny):
                pos = (x,y)
                pospx = (pad + (spaceX)*x + UIPad[0][0], pad + (spaceY)*y + UIPad[1][0])
                extendY = int((spaceY)*(y+1)) - int((spaceY)*(y)) - int(spaceY)
                cell = CellType(pos = pos, pospx = pospx, dim = (cellWidth+extendX, cellHeight+extendY), color = cellColor, state = defaultCellState)
                self._tiles.append(cell)


    def addTiles(self, *args):
        """Adds tiles to board."""
        self._objects.extend(args)
    

    def addTile(self, tile):
        """Adds tile to board."""
        self._objects.append(tile)


    def addText(self, text, txtPos, txtSize, txtColor):
        """Adds text object to window."""
        textobj = {'text': pg.font.Font(None, txtSize).render(text, color=txtColor), 'pos':txtPos}
        self._text.append(textobj)


    def addButton(self, btnPos, bntSize, CBfunc, text="Hello World!", relative=False):
        """Adds functional button."""
        if relative:
            btnPos = (btnPos[0]+self._UI['UIPos'][0], btnPos[1]+self._UI['UIPos'][1])
        button = pgui.elements.UIButton(
            relative_rect=pg.Rect(btnPos, bntSize),
            text=text,
            manager=self._manager
        )
        self._buttons[button] = CBfunc


    def addTextbox(self, boxPos, boxSize, CBfunc, relative=False):
        """Adds functional text input box."""
        if relative:
            boxPos = (boxPos[0]+self._UI['UIPos'][0], boxPos[1]+self._UI['UIPos'][1])
        textBox = pgui.elements.UITextEntryLine(
            relative_rect=pg.Rect(boxPos, boxSize),
            manager=self._manager
        )
        self._textBoxes[textBox] = CBfunc


    def _draw(self):
        """Draws inn all objects on window."""
        for tile in self._tiles:
            tile.draw(self._win)
        for obj in self._objects:
            obj.draw(self._win)
        if self._UI:
            _, _, UIColor, UIPos, UISize = self._UI.values() #UISIGNATURE
            pg.draw.rect(self._win, UIColor, (*UIPos, *UISize))
            self._manager.draw_ui(self._win)
        for textobj in self._text:
            self._win.blit(textobj['text'], textobj['pos'])

    
    def getGrid(self):
        """Returns a tile grid in matrix form, grid[j][i] is coordinate (i,j) from top left. Assumes grid is filled."""
        _, nx, ny, _, _, _, _, _, _, _ = self._mod.values() # MODSIGNATURE
        return [[self._tiles[y+ny*x] for x in range(nx)] for y in range(ny)] # j,i refers to j-th row


    def at(self, i, j):
        """Returns a tile at (i,j). Assumes grid is filled."""
        assert(0<=i<self._mod['nx'] and 0<=j<self._mod['ny'])
        return self._tiles[j+self._mod['ny']*i]

    def play(self):
        """Shows tile grid."""
        if not pg.get_init():
            pg.init()

        _, _, _, _, _, FPS, BGColor, _, _, _ = self._mod.values() # MODSIGNATURE
    
        clock = pg.time.Clock()
        running = True

        while running:
            dt = clock.tick(FPS) / 1000
            events = pg.event.get()
            self._manager.update(dt)

            self._win.fill(BGColor)
            self._draw()

            if self._action:
                self._action.update(events)
                running = self._action.running()
            for event in events:
                if event.type == pg.QUIT:
                    running = False
                if self._UI:
                    self._manager.process_events(event)
                    if event.type == pgui.UI_BUTTON_PRESSED and event.ui_element in self._buttons:
                        self._buttons[event.ui_element](self)
                    elif event.type == pgui.UI_TEXT_ENTRY_FINISHED and event.ui_element in self._textBoxes:
                        self._textBoxes[event.ui_element](self, event.text)
            
            pg.display.flip()
        pg.quit()


if __name__ == "__main__":
    import random as rd
    nx, ny = 40, 40

    def foo(TG):
        grid = TG.getGrid()
        x = rd.randint(0, nx-1)
        y = rd.randint(0, nx-1)
        print(f'({x+1}, {y+1}) is red!')
        TG.at(x,y).setColor("red")

    def faa(_, txt):
        print(txt)
    TG = TileGrid(winSize = (500,600), forceSqaure = True, nx = nx, ny = ny, UISpace = 100, UIPlace = 'bottom')
    TG.addButton((10, 30), (120, 40), foo, "Press Me", relative=True)
    TG.addTextbox((130, 30), (220, 40), faa, relative=True)
    TG.play()
