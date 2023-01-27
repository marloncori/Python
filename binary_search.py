from time import sleep

class BinarySearch(object):
    def __init__(self):
        self.array = None
        self.left = None
        self.right = None
        self.index = None
        self.element = None
        self.line = "\t---------------------------------------------------------------\n"
        
    def start_search(self, array, left, right, query):
        self.array = array
        self.left = left
        self.right = right
        self.element = query

        if self.right >= self.left:
            middle = left + (right - 1) // 2
            self.index = middle
            
            if array[self.index] == self.element:
                return self.index

            if array[self.index] > self.element:
                return self.start_search(self.array, self.left, self.index-1, self.element)

            return self.start_search(self.array, self.index+1, self.right, self.element)
        return -1

    def show(self, index):
        if index == -1:
            print("\n" + self.line)
            print("\t --> The searched element was not found in list...")
            print(self.line)
        else:
            print("\n" + self.line)
            print("\t --> The element {} is located at index # {}!".format(self.element, index))
            print(self.line)
        
        
    def __del__(self):
        print(" The end")

###############################################################################
        
binary = BinarySearch()

sequence = [23, 45, 67, 89, 11, 34]

result = binary.start_search(sequence, 0, len(sequence)-1, 67)
binary.show(result)
sleep(1)

result = binary.start_search(sequence, 0, len(sequence)-1, 12)
binary.show(result)
sleep(1)

result = binary.start_search(sequence, 0, len(sequence)-1, 89)
binary.show(result)
sleep(1)

result = binary.start_search(sequence, 0, len(sequence)-1, 34)
binary.show(result)
sleep(1)

result = binary.start_search(sequence, 0, len(sequence)-1, 23)
binary.show(result)
sleep(1)

