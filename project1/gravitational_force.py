
import stdio
import sys

# take floats as inputs
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])

# find gravitational force (in N)
g = 6.674 * 10 ** -11
f = (g * m1 * m2) / (r ** 2)

# print gravitational force
stdio.writeln(f)
