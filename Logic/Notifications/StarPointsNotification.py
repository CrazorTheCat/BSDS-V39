from Logic.Entry.ScoreEntry import ScoreEntry
from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class StarPointsNotification:
    def decode(self: Reader):
        BaseNotification.decode(self)
        for i in range(self.readVint()):
            print()
            ScoreEntry.decode(self)