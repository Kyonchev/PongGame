from button import Button


class StartButton(Button):
    def __init__(self, game, text, size, x, y):
        super().__init__(game, text, size, x, y)

    def execute(self):
        self._get_game().get_states().set_playing(True)
