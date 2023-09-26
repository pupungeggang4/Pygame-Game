import pygame
import var, const, UI, asset

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    var.screen.blit(asset.Font.neodgm_32.render('Platformer', False, const.Color.black), UI.text_title)
    pygame.display.flip()

def mouse_up(x, y, button):
    pass