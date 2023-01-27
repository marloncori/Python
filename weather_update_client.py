import sys
import zmq
from time import sleep

context = zmq.Context()
socket = context.socket(zmq.SUB)

port = 5556
print(" --> Collecting updates from weather server...")
socket.connect("tcp://192.168.0.59:" + str(port))

zipcode_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, zipcode_filter)
                         
#process thirty updates
total_temp = 0
total_hum = 0

for update in range(29):
    string = socket.recv()
    zipcode, temperature, humidity = string.split()
    total_temp += int(temperature)
    total_hum += int(humidity)
                         
    print(f"\n=====================================\n    Average temperature for zipcode\n'{zipcode_filter}' was {total_temp / (update+1)} F")
    
    print(f"\n=====================================\n    And average humidity for the same zipcode\n '{zipcode_filter}' was {total_hum / (update+1)} %")
    sleep(0.5)  
