import math
import stdio
import sys

# take latitude in degrees as float
lat = (float(sys.argv[1]))

# take longitude in degrees as float
lgt = (float(sys.argv[2]))

# claculate the values of x and y
x = lgt
y = math.log((1 + math.sin(math.radians(lat))) /
             (1 - math.sin(math.radians(lat))))/2

# write the values of x and y
stdio.write(x)
stdio.write(' ')
stdio.writeln(y)
