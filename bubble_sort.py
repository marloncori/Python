
class SortSupport(object):
    def __init__(self, name_list):
        self.length = len(name_list)
        self.last_elem = self.length-1
        self.last_one_left = 1

    def proceed_to_next(self):
        self.length -= 1

    def __del__(self):
        print(" Helper has been deleted.")
        
class Swapper(object):
    def __init__(self):
        self.first = 0
        self.second = 0

    def rearrange(self, this_elem, next_elem):
        self.first = next_elem
        self.second = this_elem
        return self.first, self.second
    
    def __del__(self):
        print(" Swapper has been dropped.")        


class Comparator(object):
    def __init__(self):
        self.first = 0
        self.second = 0

    def compare(self, this_elem, next_elem):
        self.first = this_elem
        self.second = next_elem
        if isinstance(self.first, str):
            if self.first[0] > self.second[0]:
                return 1
        else:
            if self.first > self.second:
                return 1
        return 0
    
    def __del__(self):
        print(" Comparator has been dropped.")        


class BubbleSort(object):
    def __init__(self, collection):
        self.collection = collection
        self.helper = SortSupport(collection)
        self.checker = Comparator()
        self.swapper = Swapper()
        
    def start(self):
        while self.helper.length > self.helper.last_one_left:
            for elem in range(self.helper.last_elem):
                if self.checker.compare(self.collection[elem], self.collection[elem+1]) == 1:
                    self.collection[elem], self.collection[elem+1] = self.swapper.rearrange(self.collection[elem], self.collection[elem+1])
            self.helper.proceed_to_next()
        
    def __del__(self):
        print(" Program has ended.")


names = ["Marlon", "Laura", "Beniamin", "Geysa"]
print(names)

bubble_sort = BubbleSort(names)
bubble_sort.start()

print(bubble_sort.collection, "\n")

numbers = [34, 12, 78, 4, 89, 23, 2]
print(numbers)

bubble_sorter = BubbleSort(numbers)
bubble_sorter.start()

print(bubble_sorter.collection)









