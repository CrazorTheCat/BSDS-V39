from Logic.Classes.LogicDataTables import LogicDataTables
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class PlayerDisplayData:
    Checksum = 0
    AccountBoundFlags = 0
    LogicBattleMode = "LogicBattleModeClient"
    LogicHomeMode = "LogicHomeMode"

    def decode(self: Reader):
        self.readString("PlayerName")
        self.readVint()
        self.readVint("PlayerThumbnail")
        self.readVint("NameColor")
        self.readVint()

    def encode(self: Writer):
        self.writeString(self.player.Name)
        self.writeVint(100)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(-64)

    def getNameColor(self, globalId):
        LogicDataTables.getDataById(globalId)

    def getPlayerThumbnail(self, globalId):
        LogicDataTables.getDataById(globalId)