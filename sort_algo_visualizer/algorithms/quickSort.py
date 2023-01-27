
class QuickSort:
    def __init__(self, arr):
        self.name = 'QUICK SORT'
        self.unsorted = arr
        self.arr = arr
        self.spent_time = 0.0
                
    def partition(self, arr, start, end):
        pivot = arr[end]
        i = start
        for j in range(start, end):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[end] = arr[end], arr[i]
        return i
    
    def sort(self,arr,first,last,iteration):
        if first >= last:
            return arr, 0.0
        if iteration > 0:
            start_time = time.perf_counter()
            pivot_id = self.partition(arr, first, last)
            #--------------------------------------------------------------------
            arr, self.spent_time = self.sort(arr, first, pivot_id-1, iteration-1)
            self.spent_time += time.perf_counter() - start_time
            #--------------------------------------------------------------------            
            arr, elapsed_time = self.sort(arr, pivot_id+1, last, iteration-1)
            self.spent_time += elapsed_time
        return arr, self.spent_time
    
    def start(self, iteration=0):
        return self.sort(self.arr, 0, len(self.arr)-1, iteration)
    
