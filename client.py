#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
while True:
    # print("Sending request %s …" % request)
    requestPayload = {
        "resType": "idle"
    }
    socket.send_json(requestPayload)

    #  Get the reply.
    message = socket.recv()
    print(message)