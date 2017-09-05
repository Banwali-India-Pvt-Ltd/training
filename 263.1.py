# Chapter 12
# 12.4 Class Inheritance

from countingstopwatch import CountingStopwatch
from time import sleep

timer = CountingStopwatch()
timer.start()
sleep(10)      # Pause program for 10 seconds
timer.stop()
print("Time:", timer.elapsed(), "  Number:", timer.count())

timer.start()
sleep(5)       # Pause prgram for 6 seconds
timer.stop()
print("Time:", timer.elapsed(), "  Number:", timer.count())

timer.start()
sleep(20)      # Pause program for 20 seconds
timer.stop()
print("Time:", timer.elapsed(), "  Number:", timer.count)