from stopwatch import stopwathch
class countingStopwatch (Stopwatch):
    def __init__(self):
        #Allow superclass to do its initializationn of the
        #inherited fields
        super(countingStopwatch, self).__init__()
        #set number of start message
        self.__count = 0
    def start(self):
        #count this start message
        super(countingStopwatch,self).start()
        self.__count += 1
    def rest(self):
        #Let superclass reset the inhrited fields
        super(countingStopwatch,self). reset()
        self.__count = 0
    def count(self):
        return self.__count
