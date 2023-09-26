import pygame
import sys

import var, const, UI, asset
import title, save, field

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()

    def main(self):
        var.screen = pygame.display.set_mode([1280, 720])
        pygame.display.set_caption('Card')
        self.load_font()
        self.load_image()

        while True:
            self.loop_scene()
            self.input_handle()

    def input_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                button = event.button

                if var.scene == 'title':
                    title.mouse_up(x, y, button)

                elif var.scene == 'save':
                    save.mouse_up(x, y, button)

    def loop_scene(self):
        if var.scene == 'title':
            title.loop()

    def load_font(self):
        pygame.font.init()
        asset.Font.neodgm_32 = pygame.font.Font('Font/neodgm.ttf', 32)

    def load_image(self):
        pass

if __name__ == '__main__':
    game_instance = Game()
    game_instance.main()