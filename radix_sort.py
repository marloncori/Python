import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Radix Sort Animation
class RadixSortAnimation(object):
    def __init__(self, arr):
        self.arr = arr
        self.animation = self.create_animation()

    def get_max(self, arr):
        max_val = 0
        for i in arr:
            if i > max_val:
                max_val = i
        return max_val

    def count_sort(self, arr, exp):
        output = [0] * len(arr)
        count = [0] * 10

        for i in arr:
            index = (i // exp) % 10
            count[index] += 1
        
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        i = len(arr) - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1

        for i in range(len(arr)):
            arr[i] = output[i]
    
    def radix_sort(self, arr):
        max_val = self.get_max(arr)

        exp = 1
        while max_val // exp > 0:
            self.count_sort(arr, exp)
            exp *= 10

    #Create Animation
    def create_animation(self):
        fig, ax = plt.subplots()
        arr = self.arr
        x = range(len(arr))
        bars = ax.bar(x, arr, align="edge", color='#00ffff', edgecolor='#000000')

        iteration = [0]
        def animate(arr, bars, iteration):
            for bar, val in zip(bars, arr):
                bar.set_height(val)

            iteration[0] += 1
            self.radix_sort(arr)

        ani = animation.FuncAnimation(fig, func=animate,
            fargs=(bars, iteration), frames=len(arr), 
            interval=1, repeat=False)
        plt.title('Radix Sort Animation')
        plt.xlabel('index')
        plt.ylabel('value')
        plt.tight_layout()
        return ani

# Create random array and sort it
arr = [random.randint(0, 100) for _ in range(10)]
radix_sort_animation = RadixSortAnimation(arr)
plt.show()
