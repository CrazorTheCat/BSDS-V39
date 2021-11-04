from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class FreeTextNotification:
    def decode(self: Reader):
        BaseNotification.decode(self)
        self.readVint()
