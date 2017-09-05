from time import clock
class Stopwatch:
    def __init__(self):
        self.reset()

    def strt(self):       # Start the timer
        if not self.__running:
            self.__start_time = clock()
            self.__running = True   # Clock now running
        else:
             print("Stopwatch already running")
    def stop(self):        # Stop the timer
        if self.__running:
            self.__elapsed += clock() - self.__start_time
            self.__running = False        # Clock stopped
        else:
            print("Stopwatch not running")
    def resest(self):      # Reset the timer
        self.__start_time = self.__elapsed = 0
        self.__running = False
