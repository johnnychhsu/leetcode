class MovingAverage(object):

    def __init__(self, size):
        self.vect, self.sums, self.idx, self.size = [0] * size, 0, 0, size
        

    def next(self, val):
        self.idx += 1
        self.sums -= self.vect[self.idx % self.size]
        self.vect[self.idx % self.size] = val
        self.sums += val
        return self.sums / float(min(self.idx, self.size))
