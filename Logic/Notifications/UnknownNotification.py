from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class UnknownNotification:
    def decode(self: Reader):
        BaseNotification.decode(self)
        self.readVint()
        self.readVint()
        if self.readVint() != 0:
            self.readInt()
            self.readString()
        else:
            self.readVint()
            self.readVint()
            self.readVint()
            self.readVint()
            self.readString()
