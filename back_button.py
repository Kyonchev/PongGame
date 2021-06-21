from button import Button


class BackButton(Button):
    def __init__(self, game, text, size, x, y, previous_menu):
        super().__init__(game, text, size, x, y)
        self.__previous_menu = previous_menu

    def execute(self):
        self._get_game().set_curr_menu(self.__previous_menu)
