import pygame
from paddle import Paddle


class Player(Paddle):
    def __init__(self, game):
        super().__init__(game)
        self.rect.midleft = (0, self._get_game().get_window().get_display_h() / 2)

    def draw_score(self):
        score = pygame.font.Font(self._get_game().get_font(), 20).render(str(self._score), True, self._WHITE)
        self._get_game().get_window().get_screen().blit(score, (self._get_game().get_window().get_display_w() / 4, 10))

    def update(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self._get_velocity()
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < self._get_game().get_window().get_display_h():
            self.rect.y += self._get_velocity()
