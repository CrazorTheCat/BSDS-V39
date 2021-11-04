from Logic.Classes.LogicRewardConfig import LogicRewardConfig
from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class RankedMidSeasonRewardNotification:
    def decode(self: Reader):
        BaseNotification.decode(self)
        LogicRewardConfig.decode(self)