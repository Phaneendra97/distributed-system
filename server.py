#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import os
import subprocess

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
pid = os.getpid()
isJobPresent = True

#Dummy Load
framesToBeProcessed = 160
n_cores = os.cpu_count()
print(n_cores)

# os.system("python3 client.py 1")
# subprocess.call(['open', 'Terminal.app', 'python3', '--args', 'client.py'])
# op = subprocess.run(['python3','client.py']).stdout
# print(op)
# print("he")
os.system("gnome-terminal -e 'bash -c \"python3 client.py; exec bash\"'")

while isJobPresent:
    #  Wait for next request from client
    message = socket.recv_json()
    print(message)
    if(message.get("resType") == 'idle'):
        #  Do some 'work'
        time.sleep(1)
        payload ={
            "job": "asd",
            "id": "asdaef",
            "masterPid": pid
        }
        socket.send_json(payload)
    # else if()    
