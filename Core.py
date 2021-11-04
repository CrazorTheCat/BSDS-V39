import socket
import threading
import time

from Logic.Client.ClientsManager import ClientsManager
from Logic.Data.PacketsHandler import PacketsHandler
from Logic.Client.PlayerManager import Players

class Core:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def CoreInit(self):
        self.server.bind(('0.0.0.0', 9339))
        print("Socket binded!")
        while True:
            self.server.listen()
            socket, address = self.server.accept()
            print(f'Got new connection with address: {address[0]}')
            CoreClient(socket, address).start()

class CoreClient(threading.Thread):
    def __init__(self, client, address):
        super().__init__()
        self.address = address
        self.client = client
        self.player = Players

    def run(self):
        self.last_received = time.time()
        try:
            while True:
                # Reading and processing packet
                PacketsHandler.ReadHeader(self)

        except ConnectionAbortedError:
            print(f"Client with ip: {self.address[0]} disconnected because connection was aborted!")
            ClientsManager.RemoveSocket(self.player.LowID)
            self.client.close()
            exit(0)

        except ConnectionResetError:
            print(f"Client with ip: {self.address[0]} disconnected because connection got reseted!")
            ClientsManager.RemoveSocket(self.player.LowID)
            self.client.close()
            exit(0)

        except TimeoutError:
            print(f"Client with ip: {self.address[0]} disconnected because connection got timed out!")
            ClientsManager.RemoveSocket(self.player.LowID)
            self.client.close()
            exit(0)


if __name__ == '__main__':
    server = Core()
    server.CoreInit()