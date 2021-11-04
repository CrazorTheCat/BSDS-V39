import random
import string

from Logic.Files.Classes.Cards import Cards
from Logic.Files.Classes.Characters import Characters
from Logic.Files.Classes.Locations import Locations
from Logic.Files.Classes.Skins import Skins
from Logic.Files.Classes.Pins import Pins
from Logic.Client import DevicesManager


class Players:
    HighID = 0
    LowID = 0
    Token = ""
    Name = "Guest"
    isRegistred = False
    isBanned = False

    friends = []

    trophies = 10000
    highestTrophies = 10000
    experience = 10000
    level = 500
    trophy_road_tier = 105
    coins = 9999999
    gems = 9999999
    tokens = 0
    StarTokens = 0
    StarPoints = 0

    thumbnails = 0
    nameColor = 0

    brawlerID = 0
    skinID = 0
    starpowerID = 76
    selectedSkin = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0, 46: 0, 47: 0, 49: 0, 50: 0, 51: 0, 52: 0, 53: 0}
    selectedRandomSkin = []
    brawlerState = {0: 2, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2, 11: 2, 12: 2, 13: 2, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2, 19: 2, 20: 2, 21: 2, 22: 2, 23: 2, 24: 2, 25: 2, 26: 2, 27: 2, 28: 2, 29: 2, 30: 2, 31: 2, 32: 2, 34: 2, 35: 2, 36: 2, 37: 2, 38: 2, 39: 2, 40: 2, 41: 2, 42: 2, 43: 2, 44: 2, 45: 2, 46: 2, 47: 2, 49: 2, 50: 2, 51: 2, 52: 2, 53: 2}
    allSkins = Skins.getSkinsID()
    allMaps = [5, 7, 24]
    allBrawlers = Characters.getBrawlersID()
    allBrawlersUnlock = Cards.getBrawlersUnlockID()
    allStarpowers = Cards.getStarpowersID()
    allPins = Pins.getPinsID()

    alliance_id = 0

    room_id = [0, 0]
    roomInfo = {
        "eventSlot": 0,
        "mapID": 0,
        "roomType": 0
    }

    doNotDisturb = False
    playerState = False
    lastOnline = 0

    device = DevicesManager.Device

    def CreateAccount(self, highid, lowid, token):
        if lowid == 0:
            self.HighID = int(''.join([str(random.randint(0, 9)) for _ in range(1)]))
            self.LowID = int(''.join([str(random.randint(0, 9)) for _ in range(8)]))
            self.Token = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(40))

        DBData = {
                'HighID': self.HighID,
                'LowID': self.LowID,
                'Token': self.Token,
                'name': self.Name,
                'allianceID': self.alliance_id,
                'PlayerState': self.playerState,
                'LastOnline': self.lastOnline,
                'DoNotDisturb': self.doNotDisturb,
                'brawlerID': self.brawlerID,
                'skinID': self.skinID,
                'selectedSkin': self.selectedSkin,
                'selectedRandomSkin': self.selectedRandomSkin,
                'brawlerState': self.brawlerState,
                'starpowerID': self.starpowerID,
                'playericon': self.thumbnails,
                'namecolor': self.nameColor,
                'highestTrophies': self.highestTrophies,
                'IsRegistred': self.isRegistred,
                'trophies': self.trophies,
                'experience': self.experience,
                'level': self.level,
                'gems': self.gems,
                'coins': self.coins,
                'isBanned': self.isBanned,
                'gameroomID': self.room_id,
                "roomInfo": {
                    "eventSlot": 0,
                    "mapID": 0,
                    "roomType": 0
                },
                'friend': self.friends
                }
        return DBData