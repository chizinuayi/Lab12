class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, status=False, muted=False, volume=MIN_VOLUME,  channel=MIN_CHANNEL):
        self._status = status
        self._muted = muted
        self._volume = volume
        self._channel = channel

    def power(self):
        if not self._status:
            self._status = True
        elif self._status:
            self._status = False

    def mute(self):
        if self._status:
            self._muted = not self._muted

    def channel_up(self):
        if self._status:
            if self._channel < self.MAX_CHANNEL:
                self._channel += 1
            else:
                self._channel = self.MIN_CHANNEL

    def channel_down(self):
        if self._status:
            if self._muted:
                self._muted = False
            if self._channel > self.MIN_CHANNEL:
                self._channel -= 1
            else:
                self._channel = self.MAX_CHANNEL

    def volume_up(self):
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume < self.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        if self._status:
            if self._muted:

                self._muted = False
            if self._volume > self.MIN_VOLUME:
                self._volume -= 1
            else:
                self._volume = self.MIN_VOLUME

    def muting(self):
        if self._muted:
            return 0
        else:
            return self._volume

    def __str__(self):
        return f'Power - [{self._status}], Channel - [{self._channel}], Volume - [{self.muting()}]'


