import pygame as pg

pg.init()
window = pg.display.set_mode(size=(600, 480))
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print('Quitting')
            pg.quit()
            quit()
