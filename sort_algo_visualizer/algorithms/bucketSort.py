import matplotlib.pyplot as plt

class BucketSort:
    def __init__(self, arr):
        self.name = 'BUCKET SORT'
        self.arr = arr

    def sort(self, arr, speed):
        minVal = min(arr)
        maxVal = max(arr)
        bucket_size = speed
        bucket_count = int((maxVal - minVal) / bucket_size) + 1
        buckets = [[] for _ in range(bucket_count)]
        for i in range(len(arr)):
            buckets[int((arr[i] - minVal) / bucket_size)].append(arr[i])
        arr.clear()
        for i in range(bucket_count):
            if len(buckets[i]) == 1:
                arr.append(buckets[i][0])
            else:
                self.insertion_sort(buckets[i])
                arr.extend(buckets[i])
            plt.bar(range(len(arr)), arr)
            plt.title("Bucket Sort")
            plt.pause(speed)

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def start(self):
        plt.bar(range(len(self.arr)), self.arr)
        plt.title("Initially unsorted array")
        plt.show()
        self.sort(self.arr, speed=0.05)
        plt.title("Array sorted by Bucket Sort")
        plt.show()
        