from algorithms.quickSort import QuickSort
from algorithms.mergeSort import MergeSort
from algorithms.radixSort import RadixSort
from algorithms.shellSort import ShellSort
from algorithms.bucketSort import BucketSort
from algorithms.insertSort import InsertSort
from plotter import Plotter

from time import sleep
import random

class SortAlgoApp:
    def __init__(self):
        self.plotter = None
        self.action= {
            1: QuickSort,2: MergeSort,3: RadixSort,
            4: ShellSort,5: BucketSort,6: InsertSort,
        }
        self.rand_arr = []
        self.wait_time = 2
        self.min_int = 0
        self.max_int = 100
        
    def get_data(self):
        menu ="\n\t[1] quick sort\n\t[2] merge sort\n\t[3] radix sort\n\t[4] shell sort\n\n  >> option:"
        self.cmd = int(input(" Choose one sorting algorithm: " + menu + " "))
        size = int(input("\n Okay, now tell us how many elements should be in the array: "))
        print(" ---> Processing data...")
        sleep(self.wait_time)
        self.generate_array(size)
    
    def generate_array(self, size):
        self.rand_arr = [random.randint(self.min_int,self.max_int) for _ in range(size)]

    def run(self,cmd,size):
        #self.get_data()
        self.generate_array(size)
        if not cmd in self.action.keys():
            print("   \033[1;31m [WARNING] ERROR! SORTING ALGORITHM VISUALIZATION NOT AVAILABLE!\n")
                
        for option, algorithm in self.action.items():
            if cmd == option:
                self.plotter = Plotter(algorithm(self.rand_arr))
                self.plotter.animate(speed=2)
                sleep(self.wait_time)
