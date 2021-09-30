from queue import Queue
import threading
from base import Base
from server import Server

class Sender(Base):
    def __init__(self) -> None:
        super().__init__()
        self.thread = threading.Thread(target = self.processQueue, daemon = True).start()
        self.server : Server = None

    def addToQueue(self, message : str, target : str) -> None:
        payload = {"target" : target, "message" : message}
        self.instructions.put(payload)

    def setServer(self, server : Server) -> None:
        self.server = server

    def processQueue(self) -> None:
        while True:
            #get the front item
            front = self.instructions.get()

            target = front['target']
            message = front['message']
            
            if not self.active:
                message = self.__initializeConnection__(target)

            self.server.addMessage(front)
            self.instructions.task_done()

    def __initializeConnection__(self, target : str) -> None:
        self.active = True
        msg = self.__buildRequest__(target, "", "auth")
        return msg
        
    def __buildRequest__(self, target : str, message : str, type : str):
        msg = {}
        msg['target'] = target
        msg['message'] = message

        if type == "auth":
            msg['type'] = "auth"
        elif type == "message":
            msg['type'] = "message"

        