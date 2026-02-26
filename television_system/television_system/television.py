class TelevisionSystem:

    MINIMUM_VOLUME = 0
    MAXIMUM_VOLUME = 30

    def __init__(self):
        self.__is_On = False
        self.__volume = 15
        self.__channel = 1

    def power_on(self):
        self.__is_On = True

    def power_off(self):
        self.__is_On = False

    def is_on(self):
        return self.__is_On

    def volume_up(self):
        self.__check_if_on()
        if self.__volume < self.MAXIMUM_VOLUME:
            self.__volume += 1

    def volume_down(self):
        self.__check_if_on()
        if self.__volume > self.MINIMUM_VOLUME:
            self.__volume -= 1

    def get_volume(self):
        return self.__volume

    def set_channel(self, channel):
        self.__check_if_on()
        if channel <= 0:
            raise ValueError("Invalid channel number")
        self.__channel = channel

    def get_channel(self):
        return self.__channel

    def __check_if_on(self):
        if not self.__is_On:
            raise ValueError("TV is off")