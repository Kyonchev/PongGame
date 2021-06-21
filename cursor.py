import pygame


class Cursor:
    def __init__(self, text, size, font, x_offset):
        self.__surface = pygame.font.Font(font, size).render(text, True, (255, 255, 255))
        self.__rect = pygame.Rect(-20, -20, size, size)
        self.__x_offset = x_offset

    def get_surface(self):
        return self.__surface

    def get_rect(self):
        return self.__rect

    def get_x_offset(self):
        return self.__x_offset
