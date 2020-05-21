import math
import stdio
import sys

# take three floats as inputs
x1 = (float(sys.argv[1]))
n1 = (float(sys.argv[2]))
n2 = (float(sys.argv[3]))

# find corresponding angle of refraction in degrees
x2 = math.degrees(math.asin(n1/n2 * math.sin(math.radians(x1))))

# write corresponding angle of refraction
stdio.writeln(x2)
