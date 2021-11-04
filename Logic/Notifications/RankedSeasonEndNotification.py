from Logic.Classes.LogicGemOffer import LogicGemOffer
from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class RankedSeasonEndNotification:
    def decode(self: Reader):
        BaseNotification.decode(self)
        self.readVint()
        self.readVint()
        self.readVint()
        if self.readVint() == 1:
            LogicGemOffer.decode(self)