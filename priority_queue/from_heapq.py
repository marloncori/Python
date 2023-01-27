from time import sleep
import heapq

# heapq module implements min-heap by default
# therefore the element with the smallest key 
# will be popped out first 
sbc = []

heapq.heappush(sbc, (3, 'Pine64'))
heapq.heappush(sbc, (4, 'Radxa Zero'))
heapq.heappush(sbc, (5, 'Odroid C2'))
heapq.heappush(sbc, (2, 'LattePanda'))
heapq.heappush(sbc, (7, 'Beaglebone'))
heapq.heappush(sbc, (8, 'Tinker Board'))
heapq.heappush(sbc, (1, 'Raspberry Pi 3 B+'))
heapq.heappush(sbc, (6, 'Raspberry Zero WH'))

if __name__ == '__main__':
    try:
        while sbc:
            print(heapq.heappop(sbc))
            sleep(0.5)
    except KeyboardInterrupt:
            pass