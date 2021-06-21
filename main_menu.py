from menu import Menu
from winning_score_menu import WinningScoreMenu
from credits_menu import CreditsMenu


class MainMenu(Menu):
    def __init__(self, game, header, header_size, previous):
        super().__init__(game, header, header_size, previous)
        self._get_menu_builder().add_start_button("Start Game", 20)
        self._get_menu_builder().add_to_menu_button("Winning Score", 20, WinningScoreMenu(game, "Winning Score", self))
        self._get_menu_builder().add_to_menu_button("Credits", 20, CreditsMenu(game, "Credits", self))
        self._get_menu_builder().add_exit_button("Exit", 20)
