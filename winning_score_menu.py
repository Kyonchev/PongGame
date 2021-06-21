from menu import Menu


class WinningScoreMenu(Menu):
    def __init__(self, game, header, previous):
        super().__init__(game, header, 30, previous)
        self._get_menu_builder().add_score_radio_button("Three", 20, 3)
        self._get_menu_builder().add_score_radio_button("Five", 20, 5)
        self._get_menu_builder().add_score_radio_button("Ten", 20, 10)
        self._get_menu_builder().add_back_button("Back", 20, self._get_previous_menu())

