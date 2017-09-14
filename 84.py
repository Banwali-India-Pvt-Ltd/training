from __future__ import  print_function
class Counter(object):
    def __init__(self, low, high):
         self.current = low
         self.high = high
    def __iter__(self):
         return self
    def __next__(self):
         if self.current > self.high:
            raise StopIteration
         else:
            self.current += 1
            return self.current - 1
         c = Counter(5, 10)
         for i in c:
            print(i, end=' ')