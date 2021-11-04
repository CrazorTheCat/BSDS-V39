from Logic.Notifications.BandNotification import BandNotification
from Logic.Notifications.BaseNotification import BaseNotification
from Logic.Notifications.FreeTextNotification import FreeTextNotification
from Logic.Notifications.ProLeagueSeasonEndNotification import ProLeagueSeasonEndNotification
from Logic.Notifications.PromoPopupNotification import PromoPopupNotification
from Logic.Notifications.RankedMidSeasonRewardNotification import RankedMidSeasonRewardNotification
from Logic.Notifications.RankedSeasonEndNotification import RankedSeasonEndNotification
from Logic.Notifications.SkinRewardNotification import SkinRewardNotification
from Logic.Notifications.StarPointsNotification import StarPointsNotification
from Logic.Notifications.TicketCompensationNotification import TicketCompensationNotification
from Logic.Notifications.UnknownNotification import UnknownNotification
from Logic.Notifications.VanityItemRewardNotification import VanityItemRewardNotification

notificationId = {
    2: 'DonateNotification',
    63: UnknownNotification,
    64: 'BoxRewardNotification',
    66: 'FloaterTextNotification',
    67: RankedMidSeasonRewardNotification,
    68: RankedSeasonEndNotification,
    69: 'BrawlPassAutoCollectSeasonNotification',
    71: 'BrawlPassPointRewardNotification',
    72: VanityItemRewardNotification,
    73: 'BrawlPassRewardNotification',
    74: TicketCompensationNotification,
    75: 'ChallengeSkinRewardNotification',
    76: 'QualifyNotification',
    77: ProLeagueSeasonEndNotification,
    78: 'RankRewardNotification',
    79: StarPointsNotification,
    80: 'StarPointMigrationNotification',
    81: FreeTextNotification,
    82: BandNotification,
    83: PromoPopupNotification,
    84: 'StarPowerRewardNotification',
    86: 'IAPDeliveryNotification',
    87: 'NewsPopupNotification',
    88: 'CoinDoublerRewardNotification',
    89: 'GemRewardNotification',
    90: 'ResourceRewardNotification',
    91: 'TicketRewardNotification',
    92: 'HeroPowerRewardNotification',
    93: 'HeroRewardNotification',
    94: SkinRewardNotification
}

class NotificationFactory:
    def decode(self, notificationID):
        if notificationID not in notificationId:
            BaseNotification.decode(self)
            raise NotImplementedError(f"Notification with id {notificationID} is not implemented.")
        elif type(notificationId[notificationID]) != str:
            notificationId[notificationID].decode(self)
        else:
            raise NotImplementedError(f"{notificationId[notificationID]} is not implemented.")

    def encode(self, notificationID):
        if notificationID not in notificationId:
            BaseNotification.encode(self)
            raise NotImplementedError(f"Notification with id {notificationID} is not implemented.")
        elif type(notificationId[notificationID]) != str:
            notificationId[notificationID].encode(self)
        else:
            raise NotImplementedError(f"{notificationId[notificationID]} is not implemented.")

