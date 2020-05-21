import stdio
import sys

# take month as int
m = int(sys.argv[1])

# take day as int
d = int(sys.argv[2])

# take year as int
y = int(sys.argv[3])

# finding day of the week
y0 = (int(y - (14 - m) // 12))
x0 = (int(y0 + y0 // 4 - y0 // 100 + y0 // 400))
m0 = m + 12 * ((14 - m) // 12) - 2
D = (int(d + x0 + 31 * m0 // 12) % 7)

# print day of the week
stdio.writeln(D)
