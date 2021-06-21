from abc import abstractmethod, ABC

import pygame


class Paddle(pygame.sprite.Sprite, ABC):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.__game = game
        self.__PADDLE_W = self.__game.get_window().get_display_w() / 128
        self.__PADDLE_H = self.__game.get_window().get_display_h() / 9
        self.__VELOCITY = 5
        self._score = 0
        self._WHITE = (255, 255, 255)
        self.image = pygame.Surface((self.__PADDLE_W, self.__PADDLE_H))
        self.image.fill(self._WHITE)
        self.rect = self.image.get_rect()

    def _get_game(self):
        return self.__game

    def _get_velocity(self):
        return self.__VELOCITY

    def _get_mid_y(self):
        return self.rect.y + self.__PADDLE_H / 2

    def get_rect(self):
        return self.rect

    def get_score(self):
        return self._score

    def increase_score(self):
        self._score += 1

    @abstractmethod
    def draw_score(self):
        pass
