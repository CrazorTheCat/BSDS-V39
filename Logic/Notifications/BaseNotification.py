from Logic.Data.DataManager import Writer
from Logic.Data.DataManager import Reader


class BaseNotification:
    def decode(self: Reader):
        self.readInt()
        self.readVint()
        self.readInt()
        self.readString()

    def encode(self: Writer):
        self.writeInt(0)
        self.writeVint(0)
        self.writeInt(0)
        self.writeString()

