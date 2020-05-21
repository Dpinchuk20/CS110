import stdarray
import stdio

# Read x, y, and opt from standard input.
x = stdio.readString()
y = stdio.readString()
opt = stdarray.readInt2D()

# Compute M and N.
M = len(x)
N = len(y)

# Write edit distance between x and y.
stdio.write('Edit distance = ')
stdio.writeln(opt[0][0])

# Recover and write an optimal alignment.
i = 0
j = 0
while i < M and j < N:
    # To check if w[i] is aligned with a gap
    if opt[i][j] == opt[i + 1][j] + 2:
        stdio.writeln(x[i] + ' - ' + '2')
        i += 1
    # To check if z[j] is aligned with a gap
    elif opt[i][j] == opt[i][j + 1] + 2:
        stdio.writeln('- ' + y[j] + ' 2')
        j += 1
    else:
        # To check if x[i] is aligned with y[j]
        if x[i] == y[j]:
            stdio.writeln(x[i] + ' ' + y[j] + ' 0')
        else:
            stdio.writeln(x[i] + ' ' + y[j] + ' 1')
        i += 1
        j += 1
# x is exhausted before y.
if j < N:
    stdio.writeln('- ' + y[j] + ' 2')
# y is exhausted before x.
if i < M:
    stdio.writeln('- ' + x[i] + ' 2')
