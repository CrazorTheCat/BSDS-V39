from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader

from Packets.Messages.Server.Battle.BattleEndMessage import BattleEndMessage
 
class AskForBattleEndMessage(Reader):
    def __init__(self, client, player, header_bytes):
        super().__init__(header_bytes)
        self.player = player
        self.client = client
 
    def decode(self):
        pass

    def process(self):
        BattleEndMessage(self.client, self.player).send(self.player.LowID)
