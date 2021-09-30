import queue
import os

'''
    req is dict currently but can be adapted to json v easily
    request template:
    {
        "sender" : this_id,
        "reciever" : remote_id,
        "key"    : key,
        "type"   : "auth" | "message"
        "message" : message *optional  
    }

    The key is generated via the salt 
'''

class Base():
    def __init__(self) -> None:
        self.instructions : queue.Queue = queue.Queue()
        self.salt : bytes = os.urandom(16)
        self.active : bool = False

    def close(self):
        self.instructions.join()