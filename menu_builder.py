from label import Label
from start_button import StartButton
from to_menu_button import ToMenuButton
from score_radio_button import ScoreRadioButton
from back_button import BackButton
from exit_button import ExitButton


class MenuBuilder:
    def __init__(self, game, menu, display_w, display_h):
        self.__game = game
        self.__menu = menu
        self.__mid_w, self.__mid_h = display_w / 2, display_h / 2
        self.__item_y_offset = 30

    def __increase_item_y_offset(self):
        self.__item_y_offset += 20

    def add_button_to_menu(self, button):
        self.__menu.get_buttons().append(button)
        self.__increase_item_y_offset()

    def add_label_to_menu(self, label):
        self.__menu.get_labels().append(label)
        self.__item_y_offset += 40

    def add_start_button(self, text, size):
        button = StartButton(self.__game, text, size, self.__mid_w, self.__mid_h + self.__item_y_offset)
        self.add_button_to_menu(button)

    def add_exit_button(self, text, size):
        button = ExitButton(self.__game, text, size, self.__mid_w, self.__mid_h + self.__item_y_offset)
        self.add_button_to_menu(button)

    def add_back_button(self, text, size, previous_menu):
        self.__item_y_offset += 10
        button = BackButton(self.__game, text, size, self.__mid_w, self.__mid_h + self.__item_y_offset, previous_menu)
        self.add_button_to_menu(button)

    def add_to_menu_button(self, text, size, menu):
        button = ToMenuButton(self.__game, text, size, self.__mid_w, self.__mid_h + self.__item_y_offset, menu)
        self.add_button_to_menu(button)

    def add_score_radio_button(self, text, size, value):
        button = ScoreRadioButton(self.__game, text, size, self.__mid_w, self.__mid_h + self.__item_y_offset, value)
        self.add_button_to_menu(button)

    def add_label(self, text, size):
        self.__increase_item_y_offset()
        label = Label(self.__game, text, size, self.__mid_w, self.__mid_h + self.__item_y_offset)
        self.add_label_to_menu(label)
