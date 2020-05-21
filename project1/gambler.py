import stdio
import sys

# take two integars and a float as input
n1 = (int(sys.argv[1]))
n2 = (int(sys.argv[2]))
p = (float(sys.argv[3]))

# calculate probbilities
q = 1-p
p1 = ((1 - (p/q) ** n2)) / (1 - (p/q) ** (n1 + n2))
p2 = ((1 - (q/p) ** n1)) / (1 - (q/p) ** (n1 + n2))

# write probabilities
stdio.write(p1)
stdio.write(' ')
stdio.writeln(p2)
