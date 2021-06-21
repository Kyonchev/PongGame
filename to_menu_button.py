from button import Button


class ToMenuButton(Button):
    def __init__(self, game, text, size, x, y, menu):
        super().__init__(game, text, size, x, y)
        self.__menu = menu

    def execute(self):
        self._get_game().set_curr_menu(self.__menu)

