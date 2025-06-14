from TileInterface import *
pixels_1 = [
    (5, 1), (6, 1), (7, 1), (8, 1), (9, 1),
    (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2),
    (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3),
    (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (12, 4),
    (1, 6), (7, 6), (13, 6),
    (1, 7), (7, 7), (13, 7),
    (1, 8), (2, 8), (6, 8), (7, 8), (8, 8), (12, 8), (13, 8),
    (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (12, 9), (13, 9),
    (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (11, 10), (12, 10),
    (2, 11), (3, 11), (4, 11), (5, 11), (10, 11), (11, 11), (12, 11),
    (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12),
    (5, 13), (6, 13), (7, 13), (8, 13), (9, 13)
]
pixels_2 = [
    (5, 0), (6, 0), (7, 0), (8, 0), (9, 0),
    (3, 1), (4, 1), (10, 1), (11, 1),
    (2, 2), (12, 2),
    (1, 3), (13, 3),
    (1, 4), (13, 4),
    (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5),
    (9, 5), (10, 5), (11, 5), (12, 5), (13, 5), (14, 5),
    (0, 6), (2, 6), (5, 6), (6, 6), (8, 6), (11, 6), (12, 6), (14, 6),
    (0, 7), (2, 7), (4, 7), (5, 7), (6, 7), (8, 7), (10, 7), (11, 7), (12, 7), (14, 7),
    (0, 8), (3, 8), (4, 8), (5, 8), (9, 8), (10, 8), (11, 8), (14, 8),
    (0, 9), (14, 9),
    (1, 10), (10, 10), (13, 10),
    (1, 11), (6, 11), (7, 11), (8, 11), (9, 11), (13, 11),
    (2, 12), (12, 12),
    (3, 13), (4, 13), (10, 13), (11, 13),
    (5, 14), (6, 14), (7, 14), (8, 14), (9, 14)
]


TG = TileGrid(winSize = (490,490), forceSqaure = True, nx = 15, ny = 15)
grid = TG.getGrid()
for x,y in pixels_1:
    grid[y][x].setColor("yellow")
for x,y in pixels_2:
    grid[y][x].setColor("black")

TG.play()
