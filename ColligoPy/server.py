import queue
import threading

class Server():
    #cluster is "target"
    def __init__(self) -> None:
        self.cluster : dict = {}
        self.instructions : queue.Queue = queue.Queue()
        self.thread : threading.Thread = threading.Thread(target = self.processQueue , daemon = True).start()

    #we cant type hint the object due to imports sadge
    def addNode(self, tgt_obj) -> None:
        self.cluster[tgt_obj.uuid] = tgt_obj

    def addMessage(self, message : dict) -> None:
        self.instructions.put(message)

    def processQueue(self) -> None:
        while True:
            #gets the front item
            front = self.instructions.get()
        
            #get the target of the message
            target = front['target']

            #add to the queue of the target
            self.cluster[target].input.addToQueue(front)
