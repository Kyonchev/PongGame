class States:
    def __init__(self):
        self.__running = True
        self.__playing = False
        self.__outcome = False
        self.__paused = False

    def get_running(self):
        return self.__running

    def set_running(self, boolean):
        self.__running = boolean

    def get_playing(self):
        return self.__playing

    def set_playing(self, boolean):
        self.__playing = boolean

    def get_outcome(self):
        return self.__outcome

    def set_outcome(self, boolean):
        self.__outcome = boolean

    def get_paused(self):
        return self.__paused

    def set_paused(self, boolean):
        self.__paused = boolean
