import stdio
import sys

# take three ints as input
x = (int(sys.argv[1]))
y = (int(sys.argv[2]))
z = (int(sys.argv[3]))

# find smallest, middle, and largest values
m = min(x, y, z,)
M = max(x, y, z,)
mid = (x + y + z) - (m + M)

# write numbers in ascending order
stdio.write(m)
stdio.write(' ')
stdio.write(mid)
stdio.write(' ')
stdio.writeln(M)
