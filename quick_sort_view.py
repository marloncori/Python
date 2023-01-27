import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class QuickSort(object):
    def __init__(self, array):
        self.array = array
        self.n = len(array)
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.ax.set_title('Quick Sort')
        self.ax.set_xlabel('index')
        self.ax.set_ylabel('value')

    def quick_sort(self, low, high):
        if low < high:
            pivot_index = self.partition(low, high)
            self.quick_sort(low, pivot_index - 1)
            self.quick_sort(pivot_index + 1, high)

    def partition(self, low, high):
        pivot_index = low
        pivot = self.array[high]
        for i in range(low, high):
            if self.array[i] < pivot:
                self.swap(i, pivot_index)
                pivot_index += 1
        self.swap(pivot_index, high)
        return pivot_index

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def animate(self, i):
        self.ax.clear()
        self.ax.bar(np.arange(self.n), self.array, alpha=0.3)
        self.ax.bar(i, self.array[i], alpha=1, color='g')
        self.ax.set_xlabel('index')
        self.ax.set_ylabel('value')
        self.ax.set_title('Quick Sort')
        self.ax.set_xlim([0, self.n])

    def start_animation(self):
        self.quick_sort(0, self.n - 1)
        ani = animation.FuncAnimation(self.fig, self.animate, frames=self.n, interval=200, repeat=False)
        plt.show()
        
        
array = [89, 56, 78, 23, 45, 12, 100, 37, 19, 3, 2, 1, 4, 5]
quick_sort = QuickSort(array)
quick_sort.start_animation()
       
