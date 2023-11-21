import zmq, time
from constPS import * #-

context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://0.0.0.0:"+ PORT      # how and where to communicate
s.bind(p)                          # bind socket to the address
while True:
	time.sleep(8)                    # wait every 8 seconds
	msg = str.encode("Publisher 2, time each 8 seconds" + time.asctime())
	s.send(msg) # publish the current time
