import pygame

from abc import ABC, abstractmethod


class Button(ABC):
    def __init__(self, game, text, size, x, y):
        self.__game = game
        self.__size = size
        self.__WHITE = (255, 255, 255)
        self.__surface = pygame.font.Font(self.__game.get_font(), size).render(text, True, self.__WHITE)
        self.__rect = self.__surface.get_rect()
        self.__rect.center = (x, y)

    def _get_game(self):
        return self.__game

    def get_size(self):
        return self.__size

    def get_surface(self):
        return self.__surface

    def get_rect(self):
        return self.__rect

    @abstractmethod
    def execute(self):
        pass
