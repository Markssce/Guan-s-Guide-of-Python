class Fibs():
    def __init__(self, max_):
        self.max_ = max_
        self.n, self.a, self.b = 0, 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < self.max_:
            tmp = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n += 1 # Flag
            return tmp
        raise StopIteration
for item in Fibs(10):
    print(item, end = ' ')