import matplotlib.pyplot as plt

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
        
