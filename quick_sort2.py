
class QuickSort:
    def __init__(self):
        self.pivot = None
        self.index = None
        self.p = None
        self.q = None
        self.aux = None

    def start(self, table, left, right):
        self.index = (left+right)//2
        self.pivot = table[self.index]
        self.p = left
        self.q = right
        while self.p <= self.q:
            while table[self.p] < self.pivot:
                self.p += 1
            while table[self.q] > self.pivot:
                self.q -= 1
            if self.p <= self.q:
                self.aux = table[self.p]
                table[self.p] = table[self.q]
                table[self.q] = self.aux
                self.p += 1
                self.q -= 1

        if self.q > left:
            self.start(table, left, self.q)
        if self.p < right:
            self.start(table, self.p, right)
        return table


#numbers = [78, 95, 1047, 205, 1, 4, 8, 88, 54, 31, 24, 321, 987, 741, 520, 631, 1000, 147, 45, 67, 89, 23, 14, 7]
#print(" Numbers: ", numbers)

#quick_sort = QuickSort()
#sorted_numbers = quick_sort.start(numbers, 0, len(numbers)-1)

#print(" Sorted numbers: [", end="")
#for num in sorted_numbers:
#    print(num, end= " ")
#print("]", end="")
