#!/usr/bin/env python
from plotdevice import * 
import time

start = time.time()

for x, y in grid(10,10,12,12):
    rect(x,y,10,10)

#image("/tests/", 100, 100, width=, height)

export("/Users/karen/pyprojects/prk_story/tests/trial2.png")

# this module runs super sloooooow like 10 seconds!
print "time to run: %g" % (time.time()-start)