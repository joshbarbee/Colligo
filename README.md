# Colligo

Colligo is a localized node-based network that facilitates asychronous message writing / sending. Colligo has version written in both Python and C++.

# ColligoPy

ColligoPy is the Python implementation of Colligo. The following steps documents the process to create a connection and send a message in ColligoPy
1. Within network.py, a sender object is created for sending messages, and a receiever object is used to receive messages.
2. A server is created via the server() object. The server has two nodes added to it, an identifier for the server, done via UUID(), and an identifier for the receiever.
3. The sender then adds the message to be sent to the receiver to the sender message queue via .addToQueue(). 
4. Once the message is reached in the queue by the asynchronous queue worker, it is then sent to the server. The message consists of the type of the message, the target of the message (uuid), and the message body.
5. The server then receives the message into its asynchronous queue. It reads from the queue and parses out the message target from the message string contents. 
6. The server locates the receipient via a dictionary matching UUIDs to object references, and then sends the message to the receiever.
7. The receiever adds the message to the queue. The message is eventually read via processQueue() and the output of the message saved into the .data variable of the receiver.

# ColligoC++ 

Utilizes a linked list to transmit messages in a similar manner to that of ColligoPy. Public version currently not asynchronous, as it is in development.
