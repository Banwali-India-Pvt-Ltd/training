from stopwatch import stopwathch
class countingStopwatch (Stopwatch):
    def __init__(self):
        super(countingStopwatch, self).__init__()
        self.__count = 0
    def start(self):
        super(countingStopwatch,self).start()
        self.__count += 1
    def rest(self):
        super(countingStopwatch,self). reset()
        self.__count = 0
    def count(self):
        return self.__count
