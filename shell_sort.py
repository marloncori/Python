import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Shell Sort Animation
class ShellSortAnimation(object):
    def __init__(self, arr):
        self.arr = arr
        self.animation = self.create_animation()

    # Shell Sort
    def shell_sort(self, arr):
        # Set gap between elements
        gap = len(arr) // 2
        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i
                # Shift elements of the array
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            # Reduce gap
            gap //= 2

    # Create Animation
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
            self.shell_sort(arr)

        ani = animation.FuncAnimation(fig, func=animate,
            fargs=(bars, iteration), frames=len(arr), 
            interval=1, repeat=False)
        plt.title('Shell Sort Animation')
        plt.xlabel('index')
        plt.ylabel('value')
        return ani

# Create array to sort
arr = [random.randint(0, 100) for _ in range(20)]

# Create Shell Sort Animation object
shell_sort_animation = ShellSortAnimation(arr)

# Display animation
plt.show()
