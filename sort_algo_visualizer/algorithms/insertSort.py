import matplotlib.pyplot as plt

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

