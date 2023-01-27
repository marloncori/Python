import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
import numpy as np
import random
import time

class InsertSort:
    def __init__(self, arr):
        self.name = 'INSERTION SORT'
        self.arr = arr
        self.key = 0
        self.n = 0
        
    def sort(self, arr, speed=0.4):
        self.n = len(arr)
        for i in range(1, self.n):
            self.key = arr[i]
            j = i-1
            while j >= 0 and self.key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
                plt.cla()
                plt.bar(range(len(arr)), arr)
                plt.title(f'Insertion Sort ({i+1}/{self.n})')
                plt.pause(speed)
            arr[j+1] = self.key
        plt.title('Insertion Sort (Done)')
        plt.show()

    def start(self):
        plt.bar(range(len(self.arr)), self.arr)
        plt.title('Insertion Sort (Start)')
        plt.show()
        self.sort(self.arr, speed=0.5)
        return self.arr
#------------------------------------------------------------------------------------------------
class BucketSort:
    def __init__(self, arr):
        self.name = 'BUCKET SORT'
        self.arr = arr

    def sort(self, arr, speed):
        minVal = min(arr)
        maxVal = max(arr)
        bucket_size = speed
        bucket_count = int((maxVal - minVal) / bucket_size) + 1
        buckets = [[] for _ in range(bucket_count)]
        for i in range(len(arr)):
            buckets[int((arr[i] - minVal) / bucket_size)].append(arr[i])
        arr.clear()
        for i in range(bucket_count):
            if len(buckets[i]) == 1:
                arr.append(buckets[i][0])
            else:
                self.insertion_sort(buckets[i])
                arr.extend(buckets[i])
            plt.bar(range(len(arr)), arr)
            plt.title("Bucket Sort")
            plt.pause(speed)

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def start(self):
        plt.bar(range(len(self.arr)), self.arr)
        plt.title("Initially unsorted array")
        plt.show()
        self.sort(self.arr, speed=0.05)
        plt.title("Array sorted by Bucket Sort")
        plt.show()
        return self.arr
    
#------------------------------------------------------------------------------------------------
class MergeSort:
    def __init__(self,arr):
        self.name = 'MERGE SORT'
        self.arr = arr
        self.mid = 0
        self.left_half = 0
        self.right_half = 0
        
    def sort(self, arr, speed):
        if len(arr) > 1:
            self.mid = len(arr) // 2
            self.left_half = arr[:self.mid]
            self.right_half = arr[self.mid:]

            self.sort(self.left_half, speed)
            self.sort(self.right_half, speed)

            i = 0
            j = 0
            k = 0
            while i < len(self.left_half) and j < len(self.right_half):
                if self.left_half[i] < self.right_half[j]:
                    arr[k] = self.left_half[i]
                    i += 1
                else:
                    arr[k] = self.right_half[j]
                    j += 1
                k += 1
                self.update_plot(arr, speed)

            while i < len(self.left_half):
                arr[k] = self.left_half[i]
                i += 1
                k += 1
                self.update_plot(arr, speed)

            while j < len(self.right_half):
                arr[k] = self.right_half[j]
                j += 1
                k += 1
                self.update_plot(arr, speed)

    def update_plot(self, arr, speed):
        plt.clf()
        plt.bar(range(len(arr)), arr)
        plt.title(self.name, fontsize=15, color='blue', pad=10)
        plt.pause(speed)

    def start(self):
        self.fig = plt.figure(figsize=(10,6))
        self.sort(self.arr, 0.5)
        plt.show()
        return self.arr

#------------------------------------------------------------------------------------------------
class ShellSort:
    def __init__(self, arr):
        self.name = 'SHELL SORT'
        self.unsorted = arr
        self.arr = arr
        self.spent_time = 0.0
        self.gap = len(self.arr)//2
        self.delay = 0.5
        
    def sort(self, arr, delay):
        while self.gap > 0:
            for i in range(self.gap, len(arr)):
                temp = self.arr[i]
                j = i
                # loop through the array with gap
                while j >= self.gap and arr[j-self.gap] > temp:
                    arr[j] = arr[j-self.gap]
                    j -= self.gap
                    plt.cla()
                    plt.bar(range(len(arr)),arr)
                    plt.title(self.name, fontsize=15, color='blue', pad=10)
                    plt.pause(delay)
                arr[j]=temp
            self.gap //=2
        return arr
    
    def start(self,iteration=0):
        plt.bar(range(len(self.arr)),self.arr)
        plt.title(self.name, fontsize=15, color='blue', pad=10)
        self.sort(self.arr, self.delay)
        plt.show()
        return self.arr
#------------------------------------------------------------------------------------------------        
class RadixSort:
    def __init__(self, arr):
        self.name = 'RADIX SORT'
        self.arr = arr
        self.max_val = len(self.arr)
        self.exp = 1
        self.fig = plt.figure(figsize=(10,6))
        self.barplot = plt.bar(range(len(self.arr)),self.arr,color='#6c9f9f')
        plt.title(self.name, fontsize=15, color='blue', pad=10)
        
    def sort(self, speed):
        # create a loop that iterates over the digits of the max val
        while self.max_val/self.exp > 0:
            # create a bucket for each digi
            bucket_list = [[] for _ in range(10)]
            #iterate over the dataset and append the items to the buckets
            for j in self.arr:
                index = int(j/self.exp) % 10
                bucket_list[index].append(j)
            # reassign the items to the array
            i = 0
            for bucket in bucket_list:
                for k in bucket:
                    self.arr[i] = k
                    i += 1
            #update the figure
            for rect, h in zip(self.barplot, self.arr):
                rect.set_height(h)
            # update figure and wait for the speed
            plt.title(self.name, fontsize=15, color='blue', pad=10)
            plt.pause(speed)
            #update exponent
            self.exp *= 10
            
    def start(self, speed=0.9):
        self.sort(speed)
        return self.arr
        
#------------------------------------------------------------------------------------------------
class QuickSort:
    def __init__(self, arr):
        self.name = 'QUICK SORT'
        self.unsorted = arr
        self.arr = arr
        self.spent_time = 0.0
                
    def partition(self, arr, start, end):
        pivot = arr[end]
        i = start
        for j in range(start, end):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[end] = arr[end], arr[i]
        return i
    
    def sort(self,arr,first,last,iteration):
        if first >= last:
            return arr, 0.0
        if iteration > 0:
            start_time = time.perf_counter()
            pivot_id = self.partition(arr, first, last)
            #--------------------------------------------------------------------
            arr, self.spent_time = self.sort(arr, first, pivot_id-1, iteration-1)
            self.spent_time += time.perf_counter() - start_time
            #--------------------------------------------------------------------            
            arr, elapsed_time = self.sort(arr, pivot_id+1, last, iteration-1)
            self.spent_time += elapsed_time
        return arr, self.spent_time
    
    def start(self, iteration=0):
        return self.sort(self.arr, 0, len(self.arr)-1, iteration)
    
#------------------------------------------------------------------------------------------------    
class Plotter:
    def __init__(self, sort_algorithm):
        self.sort_algorithm = sort_algorithm
        self.fig = plt.figure(figsize=(10,6))
        self.ax = self.fig.add_subplot(1,1,1)
        self.set_axes(self.sort_algorithm.arr)
        self.total_time = 0
        
    def set_axes(self, arr):
        self.ax.set_xlim([0,len(arr)])
        self.ax.set_ylim([0,max(arr)])
    
    def show(self,i):
        sorted_arr = self.sort_algorithm.start()
        self.ax.cla()
        self.set_axes(sorted_arr)
        self.ax.set_title(self.sort_algorithm.name, fontsize=15, color='blue', pad=10)
        self.ax.set_xlabel('Elements')
        self.ax.set_ylabel('Values')
        self.ax.bar(range(len(sorted_arr)),sorted_arr)
            
    def update(self, iteration):
        sorted_arr, seconds = self.sort_algorithm.start(iteration)
        if sorted_arr is not None:
            if all(sorted(self.sort_algorithm.unsorted)==sorted_arr):
                self.ax.text(0.1, 0.85, 'Sorted!',
                             horizontalalignment='left', verticalalignment='top',transform=self.ax.transAxes,fontsize=20, color='green')
                return
            
            self.ax.cla()
            self.set_axes(sorted_arr)
            self.ax.set_title(self.sort_algorithm.name, fontsize=15, color='blue', pad=10)
            self.ax.set_xlabel('Elements')
            self.ax.set_ylabel('Values')
            self.ax.bar(range(len(sorted_arr)),sorted_arr)
            self.total_time += seconds
            self.ax.text(0.55,0.95, 'Iteration: {}\nSeconds: {:.2f}\n Total Time: {:.2f}'.format(iteration, seconds, self.total_time),
                         horizontalalignment='right',verticalalignment='top',transform=self.ax.transAxes)
            
    def animate(self, speed=1):
        if self.sort_algorithm.name == 'QUICK_SORT':
            anim = animation.FuncAnimation(self.fig, self.update, frames=range(speed*len(self.sort_algorithm.arr)),
                                       interval=speed*100, repeat=False)
            plt.show()
        else:
            anim = animation.FuncAnimation(self.fig, self.show, frames=range(speed*len(self.sort_algorithm.arr)),
                                       interval=speed*100, repeat=False)
#------------------------------------------------------------------------------------------------
        
class Program:
    
    def __init__(self):
        self.sorting = None
        self.action= {
            1: QuickSort,2: MergeSort,3: RadixSort,
            4: ShellSort,5: BucketSort,6: InsertSort,
        }
        self.rand_arr = []
        self.wait_time = 2
        self.min_int = 0
        self.max_int = 100
        self.is_running=True
        
    def get_data(self):
        menu ="\n\t[1] quick sort\n\t[2] merge sort\n\t[3] radix sort\n\t[4] shell sort\n\n  >> option:"
        self.cmd = int(input(" Choose one sorting algorithm: " + menu + " "))
        size = int(input("\n Okay, now tell us how many elements should be in the array: "))
        print(" ---> Processing data...")
        time.sleep(self.wait_time)
        self.generate_array(size)
    
    def generate_array(self, size):
        self.rand_arr = [random.randint(self.min_int,self.max_int) for _ in range(size)]

    def run(self,cmd,size):
        #self.get_data()
        self.generate_array(size)
        if not cmd in self.action.keys():
                print("   \033[1;31m [WARNING] ERROR! SORTING ALGORITHM VISUALIZATION NOT AVAILABLE!\n")
                self.is_running=False
                
        for option, algorithm in self.action.items():
            if cmd == option:
                self.sorting = algorithm(self.rand_arr)
                self.plotter = Plotter(self.sorting)
                self.plotter.animate(speed=2)
                time.sleep(self.wait_time)

class UI:
    def __init__(self, app):
        self.app = app

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Sorting Algorithms")

        # Create the sorting algorithm buttons
        self.sort_label = tk.Label(self.root, text="Choose a sorting algorithm:")
        self.sp_label = tk.Label(self.root, text="                    ")
        self.quick_sort_button = tk.Button(self.root, text="QUICK SORT", command=self.on_quick_sort)
        self.merge_sort_button = tk.Button(self.root, text="MERGE SORT", command=self.on_merge_sort)
        self.radix_sort_button = tk.Button(self.root, text="RADIX SORT", command=self.on_radix_sort)
        self.shell_sort_button = tk.Button(self.root, text="SHELL SORT", command=self.on_shell_sort)
        self.bucket_sort_button = tk.Button(self.root, text="BUCKET SORT", command=self.on_bucket_sort)
        self.insert_sort_button = tk.Button(self.root, text="INSERT SORT", command=self.on_insert_sort)
        
        # Create the array size entry field
        self.size_label = tk.Label(self.root, text="Enter the size of the array:")
        self.size_entry = tk.Entry(self.root)

        self.sort_label.pack()
        # Place the widgets in the window
        self.quick_sort_button.pack()
        self.merge_sort_button.pack()
        self.radix_sort_button.pack()
        self.shell_sort_button.pack()
        self.bucket_sort_button.pack()
        self.insert_sort_button.pack()
        self.sp_label.pack()
        
        self.size_label.pack()
        self.size_entry.pack()

    def on_quick_sort(self):
        size = int(self.size_entry.get())
        self.app.run(1, size)

    def on_merge_sort(self):
        size = int(self.size_entry.get())
        self.app.run(2, size)

    def on_radix_sort(self):
        size = int(self.size_entry.get())
        self.app.run(3, size)

    def on_shell_sort(self):
        size = int(self.size_entry.get())
        self.app.run(4, size)

    def on_bucket_sort(self):
        size = int(self.size_entry.get())
        self.app.run(5, size)
        
    def on_insert_sort(self):
        size = int(self.size_entry.get())
        self.app.run(6, size)
        
    def begin(self):
        self.root.mainloop()

#------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        app = Program()
        ui = UI(app)
        ui.begin()
        
    except KeyboardInterrupt:
        print(" END OF PROGAM.")
    