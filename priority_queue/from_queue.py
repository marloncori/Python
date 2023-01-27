from time import sleep
import queue

langs = queue.PriorityQueue()

langs.put((2, "Python"))
langs.put((1, "Rust"))

langs.put((3, "C++"))
langs.put((5, "Erlang"))

langs.put((7, "Haskell"))
langs.put((6, "Javascript"))

if __name__ == '__main__':
    try:
        while not langs.empty():
            print(langs.get())
            sleep(0.3)
    except KeyboardInterrupt:
            pass