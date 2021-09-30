import threading
from base import Base
from server import Server

class Receiver(Base):
    def __init__(self) -> None:
        super().__init__()
        self.thread = threading.Thread(target = self.processQueue, daemon = True).start()
        self.server = None
        self.data = ""

    def setServer(self, server : Server) -> None:
        self.server = server

    def addToQueue(self, message : str) -> None:
        self.instructions.put(message)

    def processQueue(self) -> None:
        while True:
            #get the front item
            front = self.instructions.get()

            target = front['target']
            message = front['message']
            self.data = message

            print(self.data)

            self.instructions.task_done()
            