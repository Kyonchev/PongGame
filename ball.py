from random import randint
import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.__game = game
        self.__SIZE = 12
        self.__WHITE = (255, 255, 255)
        self.image = pygame.Surface((self.__SIZE, self.__SIZE))
        self.image.fill(self.__WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.__game.get_window().get_display_w() / 2, self.__game.get_window().get_display_h() / 2)
        self.__velocity = [randint(8, 8), randint(-8, 8)]

    def get_ball_mid_y(self):
        return self.rect.y + self.__SIZE / 2

    def __bounce_of_paddles(self):
        player, ai = self.__game.get_paddles()

        if pygame.sprite.collide_mask(self, player) or pygame.sprite.collide_mask(self, ai):
            self.__velocity[0] = -self.__velocity[0]
            self.__velocity[1] = randint(-8, 8)

    def __bounce_of_walls(self):
        player, ai = self.__game.get_paddles()

        if self.rect.right >= self.__game.get_window().get_display_w():
            self.__velocity[0] = -self.__velocity[0]
            player.increase_score()
        if self.rect.left <= 0:
            self.__velocity[0] = -self.__velocity[0]
            ai.increase_score()
        if self.rect.top <= 10:
            self.__velocity[1] = -self.__velocity[1]
        if self.rect.bottom >= self.__game.get_window().get_display_h() - 10:
            self.__velocity[1] = -self.__velocity[1]

    def update(self):
        self.__bounce_of_paddles()
        self.__bounce_of_walls()
        self.rect.x += self.__velocity[0]
        self.rect.y += self.__velocity[1]
