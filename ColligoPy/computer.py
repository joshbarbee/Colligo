from sender import Sender
from receiver import Receiver
from server import Server
import uuid
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import os

class Computer():
    def __init__(self) -> None:
        self.input = Receiver()
        self.output = Sender()
        self.uuid : str = str(uuid.uuid4())
        self.private_key = self.__generatePrivateKey()
        self.public_key = self.private_key.publickey()

    def setServer(self, server : Server):
        self.input.setServer(server)
        self.output.setServer(server)

    def sendMessage(self, message : str, target : str) -> None:
        self.output.addToQueue(message, target)

    def __generatePrivateKey(self):
        return RSA.generate(1024, os.urandom(16))

    def __decryptEncryptedMessage(self, message):
        return self.private_key.decrypt(ast.literal_eval(str(message)))

a = Computer()
b = Computer()
server = Server()

a.setServer(server)
b.setServer(server)

server.addNode(a)
server.addNode(b)

a.sendMessage("hello there", b.uuid)


