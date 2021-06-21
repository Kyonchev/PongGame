from radio_button import RadioButton


class ScoreRadioButton(RadioButton):
    def __init__(self, game, text, size, x, y, value):
        super().__init__(game, text, size, x, y, value)

    def execute(self):
        self._get_game().set_winning_score(self._get_value())
