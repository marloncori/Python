import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class BucketSort(object):
    def __init__(self, array):
        self.array = array
        self.n = len(array)
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.ax.set_title('Bucket Sort')
        self.ax.set_xlabel('index')
        self.ax.set_ylabel('value')

    def bucket_sort(self):
        # Find the minimum and maximum values in the array
        min_val = min(self.array)
        max_val = max(self.array)

        # Create a list of buckets
        buckets = [[] for _ in range(min_val, max_val + 1)]

        # Put each element in its corresponding bucket
        for i in range(self.n):
            buckets[self.array[i] - min_val].append(self.array[i])

        # Sort each bucket and then concatenate the elements in the sorted order
        sorted_array = []
        for bucket in buckets:
            if bucket:
                bucket.sort()
                sorted_array.extend(bucket)

        # Update the array with the sorted elements
        self.array = sorted_array

    def animate(self, i):
        self.ax.clear()
        self.ax.bar(np.arange(self.n), self.array, alpha=0.3)
        self.ax.bar(i, self.array[i], alpha=1, color='r')
        self.ax.set_xlabel('index')
        self.ax.set_ylabel('value')
        self.ax.set_title('Bucket Sort')
        self.ax.set_xlim([0, self.n])

    def start_animation(self):
        self.bucket_sort()
        ani = animation.FuncAnimation(self.fig, self.animate, frames=self.n, interval=200, repeat=False)
        plt.show()


array = [3, 2, 1, 4, 5]
bucket_sort = BucketSort(array)
bucket_sort.start_animation()
