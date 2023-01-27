import matplotlib.pyplot as plt

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
