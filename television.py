class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.min_volume
        self.__channel = self.min_channel

    def __str__(self):
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

    def power(self):
        if self.__status:
            self.__status = False
        elif not self.__status:
            self.__status = True

    def mute(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            elif not self.__muted:
                self.__muted = True

    def channel_up(self):
        if self.__status:
            self.__channel += 1
            if self.__channel > self.max_channel:
                self.__channel = self.min_channel

    def channel_down(self):
        if self.__status:
            self.__channel -= 1
            if self.__channel < self.min_channel:
                self.__channel = self.max_channel

    def volume_up(self):
        if self.__status:
            if self.__volume==self.max_volume:
                self.__muted=False
            else:
                self.__volume+=1
                self.__muted = False
        elif not self.__status:
            pass

    def volume_down(self):
        if self.__status:
            if self.__volume==self.min_volume:
                self.__muted = False
            else:
                self.__volume-=1
                self.__muted = False
        elif not self.__status:
            pass
