from time import sleep
import heapdict

pq = heapdict.heapdict()

# I can change the priority if I want to later on
pq['Arduino UNO'] = 3
pq['ESP-8266'] = 2
pq['Raspberry Pi Pico'] = 5
pq['ESP-32'] = 1
pq['Arduino NANO'] = 4
pq['Teensy'] = 0

if __name__ == '__main__':
    try:
        while pq:
            print(pq.popitem())
            sleep(0.3)
    except KeyboardInterrupt:
            pass