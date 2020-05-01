class TV:
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.on = False

    def turnon(self):
        self.on = True

    def turnoff(self):
        self.on = False

    def getChannel(self):
        return self.channel

    def setChannel(self, channel):
        if self.on and 1 <= self.channel <= 120:
            self.channel = channel

    def getVolumeLevl(self):
        return self.volume_level

    def setVolume(self, volume_level):
        if self.on and 1 <= self.volume_level <= 7:
            self.volume_level = volume_level

    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1

    def channelDown(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    def volumeUp(self):
        if self.on and self.volume_level < 7:
            self.volume_level += 1

    def volumeDown(self):
        if self.on and self.volume_level > 1:
            self.volume_level -= 1