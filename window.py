import pygame


class Window:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pong Game")

        self.__clock = pygame.time.Clock()
        # self.__FPS = 60

        self.__DISPLAY_W, self.__DISPLAY_H = 1280, 720
        self.__BLACK, self.__WHITE = (0, 0, 0), (255, 255, 255)
        self.__screen = pygame.display.set_mode((self.__DISPLAY_W, self.__DISPLAY_H))

    def get_clock(self):
        return self.__clock

    def get_display_w(self):
        return self.__DISPLAY_W

    def get_display_h(self):
        return self.__DISPLAY_H

    # def get_mid_w(self):
    #     return self.__DISPLAY_W / 2
    #
    # def get_mid_h(self):
    #     return self.__DISPLAY_H / 2
    #
    # def get_black(self):
    #     return self.__BLACK
    #
    # def get_white(self):
    #     return self.__WHITE

    def get_screen(self):
        return self.__screen
