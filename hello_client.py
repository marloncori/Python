import time
import zmq
import random

def read_SG90_pose():
    reading = random.uniform(2.0, 180.0)
    return reading

def publish_to_server():
    context = zmq.Context()
    publisher = context.socket(zmq.REQ)
    publisher.connect("tcp://192.168.0.59:5555")
    counter = 1
                
    while counter < 30:
        pose = read_SG90_pose()
        msg = "\n----------------------------\n [NUC] The servo motor position: {:.2f} degrees.\n----------------------------\n".format(pose)
        #publisher.send_multipart([b"A", b" The distance to object is:"])
        publisher.send_string(msg)
        time.sleep(2)
        reply = publisher.recv()
        print("\n ===> Server has answered: \n\t reply #{} {}".format(counter, reply))
        counter += 1
        time.sleep(1)
 
     
if __name__ == '__main__':
    try:
        publish_to_server()
      
    except (KeyboardInterrupt, SystemExit):
        publisher.close()
        print(" User has stopped program.")
      
       
