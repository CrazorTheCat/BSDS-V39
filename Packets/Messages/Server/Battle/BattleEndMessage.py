from Logic.Data.DataManager import Writer

class BattleEndMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.client = client
        self.player = player

    def encode(self):
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeVint(1)  # Battle End Game Mode
        self.writeVint(0)  # Result (Victory/Defeat/Draw/Rank Score)
        self.writeVint(20)  # Tokens Gained
        self.writeVint(7)  # Trophies Result
        self.writeVint(0)  # Power Play Points Gained
        self.writeVint(100)  # Doubled Tokens
        self.writeVint(50)  # Double Token Event
        self.writeVint(100)  # Token Doubler Remaining
        self.writeVint(0)  # Special Events Level Passed
        self.writeVint(0)  # Epic Win Power Play Points Gained
        self.writeVint(0)  # Championship Level Reached

        # Championship Rewards Array
        self.writeBoolean(False)  # Championship Rewards is Enabled
        # Championship Rewards Array End

        self.writeVint(0)  # Championship Losses Left
        self.writeVint(0)  # Championship Maximun Losses
        self.writeBoolean(False)  # Championship Extra Losses
        self.writeVint(200)  # Coin Shower Event
        self.writeVint(0)  # Underdog Trophies
        self.writeVint(8)  # Takedown Trophies
        self.writeVint(0)  # Defeat Trophies´
        self.writeVint(0)
        self.writeByte(11)
        self.writeVint(-64)  # Championship Challenge Type
        self.writeBoolean(False)  # Championship Cleared State

        # Players Array
        self.writeVint(3)  # Battle End Screen Players Count
        self.writeByte(0)
        self.writeDataReference(16, 53)  # Player Brawler
        self.writeDataReference(29, 0)  # Player Skin
        self.writeVint(1250)  # Brawler Trophies
        self.writeVint(1250)  # Player Power Play Points
        self.writeVint(10)  # Brawler Power Level
        self.writeVint(1)  # Brawler Power League Rank
        # Player HighID and LowID Array
        self.writeBoolean(True)  # Player HighID and LowID Array
        self.writeLong(self.player.HighID, self.player.LowID)  # Player ID
        # Player HighID and LowID Array End
        self.writeString(self.player.Name)  # Player Name
        self.writeVint(100)  # Player Experience Level
        self.writeVint(28000000 + self.player.thumbnails)  # Player Profile Icon
        self.writeVint(43000000 + self.player.nameColor)  # Player Name Color
        self.writeVint(46000000)  # Player Color Gradient if Brawl Pass is Purchased
        # Unknown Array
        self.writeBoolean(False)
        # Unknown Array End
        # Players Array End

        self.writeByte(0)
        self.writeDataReference(16, 4)  # Player Brawler
        self.writeVint(0)  # Player Skin
        self.writeVint(0)  # Brawler Trophies
        self.writeVint(0)  # Player Power Play Points
        self.writeVint(1)  # Brawler Power Level
        self.writeVint(1)  # Brawler Power League Rank
        # Player HighID and LowID Array
        self.writeBoolean(False)  # Player HighID and LowID Array
        # Player HighID and LowID Array End
        self.writeString("1")  # Player Name
        self.writeVint(100)  # Player Experience Level
        self.writeVint(28000000)  # Player Profile Icon
        self.writeVint(43000000)  # Player Name Color
        self.writeVint(46000000)  # Player Color Gradient if Brawl Pass is Purchased
        # Unknown Array
        self.writeBoolean(False)
        # Unknown Array End

        self.writeByte(0)
        self.writeDataReference(16, 51)  # Player Brawler
        self.writeVint(0)  # Player Skin
        self.writeVint(1250)  # Brawler Trophies
        self.writeVint(1250)  # Player Power Play Points
        self.writeVint(10)  # Brawler Power Level
        self.writeVint(1)  # Brawler Power League Rank
        # Player HighID and LowID Array
        self.writeBoolean(False)  # Player HighID and LowID Array
        # Player HighID and LowID Array End
        self.writeString("2")  # Player Name
        self.writeVint(100)  # Player Experience Level
        self.writeVint(28000000)  # Player Profile Icon
        self.writeVint(43000000)  # Player Name Color
        self.writeVint(46000000)  # Player Color Gradient if Brawl Pass is Purchased
        # Unknown Array
        self.writeBoolean(False)
        # Unknown Array End
        # Players Array End

        # Experience Array
        self.writeVint(2)  # Experience Gained Count
        self.writeVint(0)  # Normal Experience ID
        self.writeVint(8)  # Normal Experience Gained
        self.writeVint(8)  # Star Player Experience ID
        self.writeVint(10)  # Star Player Experience Gained
        # Experience Array End

        # Rank Up and Level Up Bonus Array
        hacc = [33, 532]
        self.writeVint(len(hacc))  # Count
        for x in range(len(hacc)):
            self.writeDataReference(39, hacc[x])  # Milestone Row
        # Rank Up and Level Up Bonus Array End

        # Milestone Progress Array
        self.writeVint(2)  # Count
        self.writeVint(1)  # Ranks Milestone ID
        self.writeVint(1246)  # Brawler Trophies
        self.writeVint(1246)  # Brawler Trophies for Rank
        self.writeVint(5)  # Experience Level Milestone ID
        self.writeVint(1262452)  # Player Experience
        self.writeVint(1262452)  # Player Experience for Level
        # Milestone Progress Array End

        self.writeDataReference(28, 0)  # Player Profile Icon

        # Play Again Status Array
        self.writeBoolean(False)  # Play Again is Enabled

        # Quests Array
        self.writeBoolean(False)  # Quests Boolean

        self.writeVint(0)
        self.writeVint(0)

        # Power League Array
        self.writeBoolean(False)  # Power League is Enabled

        self.writeVint(0)
        self.writeBoolean(False)