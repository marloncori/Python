import matplotlib.pyplot as plt

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
