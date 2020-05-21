import math
import stdio
import sys

# take four floats as imput
x1 = (float(sys.argv[1]))
y1 = (float(sys.argv[2]))
x2 = (float(sys.argv[3]))
y2 = (float(sys.argv[4]))

# find great circle distance
d = 111 * math.degrees(math.acos(math.sin(math.radians(x1)) *
                                 math.sin(math.radians(x2))
                                 + math.cos(math.radians(x1))
                                 * math.cos(math.radians(x2))
                                 * math.cos(math.radians(y1-y2))))

# print great circle distance
stdio.writeln(d)
