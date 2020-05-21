import stdio
import sys

# take two floats as inputs
t = (float(sys.argv[1]))
v = (float(sys.argv[2]))

# find the wind chill
w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v ** 0.16

# write the wind chill
stdio.writeln(w)

