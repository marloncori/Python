from time import sleep

class Program:
    
    FIRST  = 0
    SECOND = 1
    WAIT   = 1
    
    def __init__(self, i=7):
        self.i = i
        self.action= {
            'U': [lambda i: i+1, lambda : print(" ---> Robot has move one cell up!")],
            'L': [lambda i: i-1, lambda : print(" ---> Robot has move one cell left!")],
            'R': [lambda j: j+1, lambda : print(" ---> Robot has move one cell right!")],
            'D': [lambda j: j-1, lambda : print(" ---> Robot has move one cell down!")],
        }

    def get_data(self):
        menu ="\n\t[U] move up\n\t[L] turn right\n\t[R] turn left\n\t[D] move down\n\n  >> option:"
        self.cmd = str(input(" Enter command: " + menu + " ")).strip().upper()
        
    def move_bot(self):
        if not self.cmd in self.action.keys():
                print("   \033[1;31m [ROS] ERROR! COMMAND NOT RECOGNISED... Stopping motors...\033[0m\n")
                return
        for key, func in self.action.items():
            if self.cmd == key:
                func[self.FIRST](self.i)
                print(" [ROS] Robot has sent a message:\n\t")
                sleep(self.WAIT)
                func[self.SECOND]()
                sleep(self.WAIT)
                
    def moved_cm(self):
        print(f" [ROS] Covered distance:\n\t >>> {self.i*10} cm.")

def run():
    app = Program()
    app.get_data()
    app.move_bot()
    app.moved_cm()

if __name__ == '__main__':
    try:
        while True:
            run()
            
    except KeyboardInterrupt:
        print(" Program has been stopped.")