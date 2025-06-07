import pygame as pg
import numpy as np

class Tile():
    """Basic tile class."""
    def __init__(self, pos:tuple = (0,0), pospx:tuple = (0,0), dim:tuple = (10,10), color:str = "black", state = None):
        """Constructor."""
        self._pos = pos
        self._pospx = pospx
        self._dim = dim
        self._color = color
        self._state = state
    

    def draw(self, win):
        """Class funciton to draw cell on window."""
        pg.draw.rect(win,self._color,(*self._pospx,*self._dim))


    def setState(self, state):
        """Update cell state."""
        self._state = state

    def setColor(self, color):
        """Updates color of cell."""
        self._color = color


class TileInterface():
    """Visual interface with pygame"""
    def __init__(self):
        """Constructor"""


class TileGrid():
    """Vidsial tile grid with pygame"""
    def __init__(self, mod = None, fillTiles = True, action = None, **kwargs):
        """Constructor"""
        self._tiles = []
        #self._grid = []
        self._objects = []
        self._action = action # game goes here

        if mod is not None:
            self._mod = mod
        else:  
            # size, nx, ny, pad, Cpad, FPS, BGColor, Ccolor, Cstate, square = self._mod.values() 
            self._mod = {
            'size':(1000,500),
            'nx':10,
            'ny':5,
            'padding':5,
            'cellPadding':1,
            'FPS':30,
            'BGColor':(65,65,65),
            'CellColor':"white",
            'baseCellState':None,
            'forceSqaure':False
            }

            for key, value in kwargs.items():
                if self._mod.__contains__(key):
                    self._mod[key] = value
        
        if (fillTiles): self.fillTiles(Tile)


    def fillTiles(self, CellType:type = Tile):
        """Fills inn board with grid tiles of spesific type."""

        size, nx, ny, pad, Cpad, _, _, Ccolor, Cstate, square = self._mod.values() 
        width, height = size

        cellWidth = int((width-2*pad-(nx-1)*Cpad)/nx)
        cellHeight = int((height-2*pad-(ny-1)*Cpad)/ny)

        if square:
            cellWidth, cellHeight = min(cellWidth, cellHeight), min(cellWidth, cellHeight)

        for x in range(nx):
            #self._grid.append([])
            for y in range(ny):
                pos = (x,y)
                pospx = (pad + (cellWidth+Cpad)*x, pad + (cellHeight+Cpad)*y)
                cell = CellType(pos = pos, pospx = pospx, dim = (cellWidth,cellHeight), color = Ccolor, state = Cstate)
                self._tiles.append(cell)
                #self._grid[-1].append(cell)


    def addTiles(self, *args):
        """Adds tiles to board"""
        self._objects.extend(args)

    
    def _draw(self, win):
        """Draws inn all objects on grid"""
        for tile in self._tiles:
            tile.draw(win)
        for obj in self._objects:
            obj.draw(win)

    
    def getGrid(self):
        """Returns a tile grid in matrix form."""
        _, nx, ny, _, _, _, _, _, _, _ = self._mod.values() 
        return [[self._tiles[y+ny*x] for x in range(nx)] for y in range(ny)]


    def play(self):
        """Shows tile grid."""
        size, _, _, _, _, FPS, BGColor, _, _, _ = self._mod.values() 

        pg.init()
        doAction = self._action is not None
        screen = pg.display.set_mode(size)
        clock = pg.time.Clock()
        running = True

        while running:
            events = pg.event.get()
            screen.fill(BGColor)
            self._draw(screen)

            if doAction:
                self._action.update(events)
                running = self._action.running()
            for event in events:
                if event.type == pg.QUIT:
                    running = False

            pg.display.flip()
            clock.tick(FPS)
        
        pg.quit()


if __name__ == "__main__":
    TG = TileGrid(size = (1200,600), forceSqaure = False, nx = 41, ny = 21)
    TG.play()


