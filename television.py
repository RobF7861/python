class Television:
    min_volume:int = 0
    max_volume:int = 2
    min_channel:int = 0
    max_channel:int = 3

    def __init__(self):
        '''
        Creates a TV
        '''
        self.__status:bool = False
        self.__muted:bool = False
        self.__volume:int = self.min_volume
        self.__channel:int = self.min_channel

    def __str__(self):
        '''
        Returns formatted string of TV conditions
        '''
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

    def power(self):
        '''
        Flips condition of TV power
        '''
        if self.__status:
            self.__status = False
        elif not self.__status:
            self.__status = True

    def mute(self):
        '''
        Mutes/unmutes TV
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
            elif not self.__muted:
                self.__muted = True

    def channel_up(self):
        '''
        Increases channel value
        Returns to the lowest value if channel value exceeds max value
        '''
        if self.__status:
            self.__channel += 1
            if self.__channel > self.max_channel:
                self.__channel = self.min_channel

    def channel_down(self):
        '''
        Decreases channel value
        Returns to the highest value if channel value exceeds min value
        '''
        if self.__status:
            self.__channel -= 1
            if self.__channel < self.min_channel:
                self.__channel = self.max_channel

    def volume_up(self):
        '''
        Increases volume value
        Unmutes TV
        Value is set to max volume if max is exceeded
        '''
        if self.__status:
            if self.__volume==self.max_volume:
                self.__muted=False
            else:
                self.__volume+=1
                self.__muted = False
        elif not self.__status:
            pass

    def volume_down(self):
        '''
        Decreases volume value
        Unmutes TV
        Value is set to min volume if min is exceeded
        '''
        if self.__status:
            if self.__volume==self.min_volume:
                self.__muted = False
            else:
                self.__volume-=1
                self.__muted = False
        elif not self.__status:
            pass
