

# Use while loop as follows to run from 1 (i=1) to infinity
# The following will run infinity times
import time
i=1
while True:
	print "Welcome", i, "times. To stop press [CTRL+C]"
	i += 1
        # Delay for 2 seconds
        time.sleep(2)