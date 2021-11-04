from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class ScoreEntry:
    def decode(self: Reader):
        self.readVint()
        self.readVint()
        self.readVint()
        self.readVint()