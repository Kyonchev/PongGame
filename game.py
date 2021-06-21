import sys
import pygame

from ai import Ai
from ball import Ball
from keys import Keys
from main_menu import MainMenu
from player import Player
from states import States
from window import Window


class Game:
    def __init__(self):
        self.__window = Window()
        self.__states = States()
        self.__keys = Keys()

        self.__font = "8-BIT WONDER.TTF"
        self.__WHITE = (255, 255, 255)
        self.__BLACK = (0, 0, 0,)

        self.__main_menu = MainMenu(self, "Pong Game", 40, None)
        self.__curr_menu = self.__main_menu

        self.__ball, self.__player, self.__ai, self.__all_sprites = None, None, None, None

        self.__winning_score = 3

    def get_window(self):
        return self.__window

    def get_states(self):
        return self.__states

    def get_keys(self):
        return self.__keys

    def get_font(self):
        return self.__font

    def get_ball(self):
        return self.__ball

    def get_paddles(self):
        return self.__player, self.__ai

    def set_curr_menu(self, curr_menu):
        self.__curr_menu = curr_menu

    def set_winning_score(self, score):
        self.__winning_score = score

    def exit(self):
        pygame.quit()
        sys.exit()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.__keys.set_return_key(True)
                if event.key == pygame.K_ESCAPE:
                    self.__keys.set_escape_key(True)
                if event.key == pygame.K_UP:
                    self.__keys.set_up_key(True)
                if event.key == pygame.K_DOWN:
                    self.__keys.set_down_key(True)
                if event.key == pygame.K_x:
                    self.__keys.set_x_key(True)

    def __draw_label(self, text, size, x, y):
        text_surface = pygame.font.Font("8-BIT WONDER.TTF", size).render(text, True, self.__WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.__window.get_screen().blit(text_surface, text_rect)

    def __draw_mid_line(self):
        pygame.draw.line(self.__window.get_screen(), self.__WHITE, [self.__window.get_display_w() / 2, 0],
                         [self.__window.get_display_w() / 2, self.__window.get_display_h()], 1)

    def __draw_circle(self):
        pygame.draw.circle(self.__window.get_screen(), self.__WHITE, self.__ball.rect.center, 12)

    def __draw_gameplay(self):
        self.__window.get_screen().fill(self.__BLACK)
        self.__draw_mid_line()
        self.__draw_circle()
        self.__player.draw_score()
        self.__ai.draw_score()
        self.__all_sprites.draw(self.__window.get_screen())
        pygame.display.update()

    def __pause(self):
        self.__draw_label("Game is Paused", 20, self.__window.get_display_w() / 2, self.__window.get_display_h() / 2)
        self.__draw_label("Press ESC to continue or x to quit to main menu", 20, self.__window.get_display_w() / 2,
                          self.__window.get_display_h() / 2 + 30)

        while self.__states.get_paused():
            self.__keys.reset_keys()
            self.check_events()

            if self.__keys.get_x_key():
                self.__states.set_playing(False)
                self.__states.set_paused(False)
            if self.__keys.get_escape_key():
                self.__states.set_paused(False)

            pygame.display.update()

    def __check_game_outcome(self):
        if self.__player.get_score() == self.__winning_score or self.__ai.get_score() == self.__winning_score:
            self.__states.set_outcome(True)
            self.__window.get_clock().tick(5)

            if self.__player.get_score() == self.__winning_score:
                self.__draw_label("You are the Winner", 20, self.__window.get_display_w() / 2,
                                  self.__window.get_display_h() / 2)
            elif self.__ai.get_score() == self.__winning_score:
                self.__draw_label("The AI is the Winner", 20, self.__window.get_display_w() / 2,
                                  self.__window.get_display_h() / 2)
            self.__draw_label("Press x to quit", 20, self.__window.get_display_w() / 2,
                              self.__window.get_display_h() / 2 + 30)
            pygame.display.update()

            while self.__states.get_outcome():
                self.check_events()
                if self.__keys.get_x_key():
                    self.__states.set_playing(False)
                    self.__states.set_outcome(False)
                self.__keys.reset_keys()

    def __update_sprites(self):
        self.__all_sprites.update()

    def game_loop(self):
        self.__ball = Ball(self)
        self.__player = Player(self)
        self.__ai = Ai(self)
        self.__all_sprites = pygame.sprite.Group(self.__player, self.__ai, self.__ball)

        while self.__states.get_playing():
            self.__window.get_clock().tick(60)
            self.check_events()
            if self.__keys.get_escape_key():
                self.__states.set_paused(True)
                self.__pause()

            self.__check_game_outcome()
            self.__update_sprites()
            self.__draw_gameplay()
            self.__keys.reset_keys()

    def run(self):
        while self.get_states().get_running():
            self.__curr_menu.display_menu()
            self.game_loop()
