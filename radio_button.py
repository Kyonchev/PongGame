from abc import abstractmethod

from button import Button


class RadioButton(Button):
    def __init__(self, game, text, size, x, y, value):
        super().__init__(game, text, size, x, y)
        self.__value = value

    def _get_value(self):
        return self.__value

    @abstractmethod
    def execute(self):
        pass
