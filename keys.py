class Keys:
    def __init__(self):
        self.__RETURN_KEY = False
        self.__ESCAPE_KEY = False
        self.__UP_KEY = False
        self.__DOWN_KEY = False
        self.__X_KEY = False

    def get_return_key(self):
        return self.__RETURN_KEY

    def set_return_key(self, return_key):
        self.__RETURN_KEY = return_key

    def get_escape_key(self):
        return self.__ESCAPE_KEY

    def set_escape_key(self, escape_key):
        self.__ESCAPE_KEY = escape_key

    def get_up_key(self):
        return self.__UP_KEY

    def set_up_key(self, up_key):
        self.__UP_KEY = up_key

    def get_down_key(self):
        return self.__DOWN_KEY

    def set_down_key(self, down_key):
        self.__DOWN_KEY = down_key

    def get_x_key(self):
        return self.__X_KEY

    def set_x_key(self, x):
        self.__X_KEY = x

    def reset_keys(self):
        self.__RETURN_KEY = False
        self.__ESCAPE_KEY = False
        self.__UP_KEY = False
        self.__DOWN_KEY = False
        self.__X_KEY = False
