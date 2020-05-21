import math
import stdio
import sys

# take two floats as input
x1 = (float(sys.argv[1]))
n1 = (float(sys.argv[2]))

# find the probability
P = math.exp(-x1 * n1)

# write the probability
stdio.writeln(P)
