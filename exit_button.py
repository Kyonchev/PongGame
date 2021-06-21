from button import Button


class ExitButton(Button):
    def __init__(self, game, text, size, x, y):
        super().__init__(game, text, size, x, y)

    def execute(self):
        self._get_game().exit()
