from sender import Sender
from receiver import Receiver
from server import Server

sender = Sender()
receiver = Receiver()
server = Server()

server.addNode(sender.uuid, sender)
server.addNode(receiver.uuid, receiver)
receiver.server = server
sender.server = server

sender.addToQueue("hello sender", receiver.uuid)

sender.close()
receiver.close()