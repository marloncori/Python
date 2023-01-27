
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# MergeSort Animation
class MergeSortAnimation(object):
    def __init__(self, arr):
        self.arr = arr
        self.aux = [0] * len(arr)
        self.animation = self.create_animation()

    # Merge two parts of the array
    def merge(self, arr, l, m, r): 
        n1 = m - l + 1
        n2 = r - m 
  
        # Create temp arrays 
        L = [0] * n1 
        R = [0] * n2 
  
        # Copy data to temp arrays L[] and R[] 
        for i in range(0, n1): 
            L[i] = arr[l + i] 
  
        for j in range(0, n2): 
            R[j] = arr[m + 1 + j] 
  
        # Merge the temp arrays back into arr[l..r] 
        i = 0     # Initial index of first subarray 
        j = 0     # Initial index of second subarray 
        k = l     # Initial index of merged subarray 
  
        while i < n1 and j < n2: 
            if L[i] <= R[j]: 
                arr[k] = L[i] 
                i += 1
            else: 
                arr[k] = R[j] 
                j += 1
            k += 1
  
        # Copy the remaining elements of L[], if there 
        # are any 
        while i < n1: 
            arr[k] = L[i] 
            i += 1
            k += 1
  
        # Copy the remaining elements of R[], if there 
        # are any 
        while j < n2: 
            arr[k] = R[j] 
            j += 1
            k += 1

    # Merge Sort
    def merge_sort(self, arr, l, r): 
        if l < r: 
            m = int((l+(r-1))/2)
  
            # Sort first and second halves 
            self.merge_sort(arr, l, m) 
            self.merge_sort(arr, m+1, r) 
            self.merge(arr, l, m, r) 

    #Create Animation
    def create_animation(self):
        fig, ax = plt.subplots()
        arr = self.arr
        x = range(len(arr))
        bars = ax.bar(x, arr, align="edge", color='#00ffff', edgecolor='#000000')

        iteration = [0]
        def animate(i, arr, bars, iteration):
            for bar, val in zip(bars, arr):
                bar.set_height(val)

            iteration[0] += 1
            self.merge_sort(arr, 0, len(arr)-1)

        ani = animation.FuncAnimation(fig, func=animate,
            fargs=(arr, bars, iteration), frames=len(arr), 
            interval=1, repeat=False)
        plt.title('Merge Sort Animation')
        plt.xlabel('index')
        plt.ylabel('value')
        return ani


# Driver Code
if __name__ == '__main__':
    arr = [random.randint(0,100) for i in range(25)]
    print('Array Before Sort: ', arr)
    merge_sort_animation = MergeSortAnimation(arr)
    anim = merge_sort_animation.create_animation()
    plt.show()
    print('Array After Sort: ', arr)