#!/usr/bin/env python
# enoding: utf-8
import time
start = time.time()

from plotdevice import *

print "time to import: %g" % (time.time()-start)

size(600, 600)
color(mode=RGB, range=255)
background(0,75)
clear(all)

svg = ximport("svg")
sf_paths = svg.parse(open('/Users/karen/pyprojects/prk_story/tests/sf36.svg').read())
sf_path = sf_paths[0] # there is a single path in here so we select just that one!

def sf_correction(path, x, y):
    x_offset = 0
    y_offset = -30
    return x-path.center.x+x_offset, y-path.center.y+y_offset

#arc(WIDTH/2, (HEIGHT/2)+30, 5) # true canvas center

sf_path.translate(*sf_correction(sf_path, WIDTH/2, HEIGHT/2))
sf_path.scale(3)

# note: the drawpath method doesn't return anything bc type=nonetype.
drawpath(sf_path.copy(), fill=("white",.75), stroke="black", strokewidth=.5) # this actually draw the shape

with clip(sf_path):
    geometry(PERCENT)
    total_ratio = 0.05
    rotate(.17)
    arc(WIDTH/2, (HEIGHT/2)+30, 275, range=total_ratio, fill=('red',.5), close=True)

reset()
text("The Rest of San Francisco",140,430,fontsize=16,family="Hammersmith One")
text("Parking",392,190,fontsize=12,family="Hammersmith One")
#export("/Users/karen/pyprojects/prk_story/tests/sf_paths.pdf")


