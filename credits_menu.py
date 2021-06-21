from menu import Menu


class CreditsMenu(Menu):
    def __init__(self, game, header, previous):
        super().__init__(game, header, 30, previous)
        self._get_menu_builder().add_label("Made by Kalin Yonchev", 20)
        self._get_menu_builder().add_back_button("Back", 20, self._get_previous_menu())

