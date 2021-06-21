import pygame

from paddle import Paddle


class Ai(Paddle):
    def __init__(self, game):
        super().__init__(game)
        self.rect.midright = (
            self._get_game().get_window().get_display_w(), self._get_game().get_window().get_display_h() / 2)

    def draw_score(self):
        score = pygame.font.Font(self._get_game().get_font(), 20).render(str(self._score), True, self._WHITE)
        self._get_game().get_window().get_screen().blit(score, (
            self._get_game().get_window().get_display_w() / 2 + self._get_game().get_window().get_display_w() / 4, 10))

    def update(self):
        ai_mid_y = self._get_mid_y()
        ball_mid_y = self._get_game().get_ball().get_ball_mid_y()
        if ai_mid_y > ball_mid_y and self.rect.y > 0:
            self.rect.y -= self._get_velocity()
        if ai_mid_y < ball_mid_y and self.rect.y < self._get_game().get_window().get_display_h():
            self.rect.y += self._get_velocity()
