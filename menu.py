import pygame

from collections import deque
from cursor import Cursor
from label import Label
from menu_builder import MenuBuilder
from score_radio_button import ScoreRadioButton


class Menu:
    def __init__(self, game, header, header_size, previous):
        self.__game = game
        self.__previous_menu = previous

        self.__cursor = Cursor("*", 15, self.__game.get_font(), -25)
        self.__selected = Cursor("*", 15, self.__game.get_font(), 25)

        self.__header_y_offset = -30
        self.__header = Label(self.__game, header, header_size, self.__game.get_window().get_display_w() / 2,
                              self.__game.get_window().get_display_h() / 2 + self.__header_y_offset)
        self._buttons = deque()
        self._labels = deque()

        self._curr_button = None
        self._first_item = None
        self._selected_radio_button = None

        self.__menu_builder = MenuBuilder(self.__game, self, game.get_window().get_display_w(),
                                          game.get_window().get_display_h())

    def _get_game(self):
        return self.__game

    def _get_previous_menu(self):
        return self.__previous_menu

    def get_buttons(self):
        return self._buttons

    def get_labels(self):
        return self._labels

    def _get_menu_builder(self):
        return self.__menu_builder

    def _draw_label(self, label):
        self.__game.get_window().get_screen().blit(label.get_surface(), label.get_rect())

    def _draw_button(self, button):
        self.__game.get_window().get_screen().blit(button.get_surface(), button.get_rect())

    def _draw_cursor(self):
        self.__game.get_window().get_screen().blit(self.__cursor.get_surface(), self.__cursor.get_rect())

    def _draw_selected_radio_button(self):
        self.__game.get_window().get_screen().blit(self.__selected.get_surface(), self.__selected.get_rect())

    def _check_return_key(self):
        if not self._first_item:
            self._first_item = self._buttons[0]

        if self.__game.get_keys().get_return_key():
            self._curr_button.execute()

            if isinstance(self._curr_button, ScoreRadioButton):
                x, y = self._curr_button.get_rect().midright
                self.__selected.get_rect().midleft = (x + self.__selected.get_x_offset(), y)
            else:
                while self._buttons[0] != self._first_item:
                    self._buttons.rotate(-1)

    def _move_cursor(self):
        if self.__game.get_keys().get_up_key():
            self._buttons.rotate(1)
        elif self.__game.get_keys().get_down_key():
            self._buttons.rotate(-1)

        self._curr_button = self._buttons[0]
        x, y = self._curr_button.get_rect().midleft
        self.__cursor.get_rect().midright = (x + self.__cursor.get_x_offset(), y)

    def _update_screen(self):
        pygame.display.update()
        self.__game.get_keys().reset_keys()

    def display_menu(self):
        self._get_game().check_events()
        self._check_return_key()
        self._move_cursor()
        self.__game.get_window().get_screen().fill((0, 0, 0))
        self._draw_label(self.__header)
        for label in self._labels:
            self._draw_label(label)
        for button in self._buttons:
            self._draw_button(button)
        self._draw_cursor()
        self._draw_selected_radio_button()
        self._update_screen()
