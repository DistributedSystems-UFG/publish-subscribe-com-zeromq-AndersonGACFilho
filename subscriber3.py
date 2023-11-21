import zmq
from constPS import * #-

context = zmq.Context()
s1 = context.socket(zmq.SUB)          # create a subscriber socket
p1 = "tcp://"+ HOST1 +":"+ PORT        # how and where to communicate
s1.connect(p1)                         # connect to the server
s1.setsockopt_string(zmq.SUBSCRIBE, "TIME")  # subscribe to TIME messages

s2 = context.socket(zmq.SUB)          # create a subscriber socket
p2 = "tcp://"+ HOST2 +":"+ PORT        # how and where to communicate
s2.connect(p2)                         # connect to the server
s2.setsockopt_string(zmq.SUBSCRIBE, "TIME")  # subscribe to TIME messages

for i in range(5):  # Five iterations
	time = s1.recv() + "\r\n" + s2.recv()   # receive a message
	print (bytes.decode(time))