import heapq
class NumberContainers:

    def __init__(self):
        self.indices = {}
        self.numbers = collections.defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:

        if index not in self.indices:
            self.indices[index] = number
        else:
            if self.indices[index] != number:
                self.numbers[self.indices[index]].remove(index)
                if not self.numbers[self.indices[index]]:
                    del self.numbers[self.indices[index]]
                self.indices[index] = number

        self.numbers[number].add(index)

    def find(self, number: int) -> int:

        if number not in self.numbers:
            return -1
        else:
            if not self.numbers[number]: return -1
            return self.numbers[number][0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)