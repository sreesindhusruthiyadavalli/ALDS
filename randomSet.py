class Set():
    def __init__(self):
        self.dst = {}
        self.indexDst = {}
        self.lst = []
        return

    def insert(self, val):
        if val in self.dst:
            return False
        self.dst[val] = True
        self.lst.append(val)
        self.indexDst[val] = len(self.lst) - 1
        return True

    def remove(self, val):
        if val in self.dst:
            del self.dst[val]
            self.lst[self.indexDst[val]
                     ], self.lst[-1] = self.lst[-1], self.lst[self.indexDst[val]]
            # [1,6,3,4,5] {6:0}
            self.lst.pop()
            self.indexDst[self.lst[self.indexDst[val]]] = self.indexDst[val]
            del self.indexDst[val]
            return True
        return False

    def giverandom(self):
        length = len(self.dst.keys())
        #randIndex = random.randint(0, length-1)
        return self.lst[-1]

    def printtemp(self):
        print(self.dst, self.indexDst, self.lst)


set = Set()
set.insert(1)
set.insert(6)
set.insert(3)
set.insert(4)
set.insert(5)
set.printtemp()
set.remove(6)
set.printtemp()
print(set.giverandom())
