import zmq
from constPS import * #-

context = zmq.Context()
s2 = context.socket(zmq.SUB)          # create a subscriber socket
p2 = "tcp://"+ HOST2 +":"+ PORT        # how and where to communicate
s2.connect(p2)                         # connect to the server
s2.setsockopt_string(zmq.SUBSCRIBE, "TIME")  # subscribe to TIME messages

for i in range(5):  # Five iterations
	time = s.recv()   # receive a message
	print (bytes.decode(time))
