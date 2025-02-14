class ProductOfNumbers:

    def __init__(self):
        self.li = []
        self.d = []

    def add(self, num: int) -> None:
        if num == 0 :
            self.li = []
            self.d = []
        else:
            if len(self.li) != 0:
                self.d.append(self.d[-1]*num)
            else:
                self.d.append(num)
            self.li.append(num)

    def getProduct(self, k: int) -> int:
        if k>len(self.li):
            return 0
        elif k == len(self.li):
            return self.d[-1]
        else:
            return self.d[-1] // self.d[len(self.d) - (k+1)]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)