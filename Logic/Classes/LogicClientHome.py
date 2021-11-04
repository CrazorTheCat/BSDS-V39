from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader
from Logic.Classes.LogicConfData import LogicConfData
from Logic.Classes.LogicDailyData import LogicDailyData


class LogicClientHome:
    def decode(self: Reader):
        pass

    def encode(self: Writer):
        LogicDailyData.encode(self)
        LogicConfData.encode(self)
        self.writeLong(self.player.HighID, self.player.LowID)  # PlayerID
        self.writeVint(0) # Notification Factory
        self.writeVint(-64)  # VideoAdStarted
        self.writeBoolean(False)
        self.writeVint(0)  # GatchaDrop
        self.writeVint(0)  # FriendlyStarPower