
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class InsertionSort(object):
    def __init__(self, array):
        self.array = array
        self.n = len(array)
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.ax.set_title('Insertion Sort')
        self.ax.set_xlabel('index')
        self.ax.set_ylabel('value')

    def insertion_sort(self):
        for i in range(1, self.n):
            for j in range(i, 0, -1):
                if self.array[j] < self.array[j - 1]:
                    self.swap(j, j - 1)
                else:
                    break

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def animate(self, i):
        self.ax.clear()
        self.ax.bar(np.arange(self.n), self.array, alpha=0.3)
        self.ax.bar(i - 1, self.array[i - 1], alpha=1, color='r')
        self.ax.bar(i, self.array[i], alpha=1, color='g')
        self.ax.set_xlabel('index')
        self.ax.set_ylabel('value')
        self.ax.set_title('Insertion Sort')
        self.ax.set_xlim([0, self.n])

    def start_animation(self):
        self.insertion_sort()
        ani = animation.FuncAnimation(self.fig, self.animate, frames=self.n, interval=200, repeat=False)
        plt.show()


array = [3, 2, 1, 4, 5]
insertion_sort = InsertionSort(array)
insertion_sort.start_animation()