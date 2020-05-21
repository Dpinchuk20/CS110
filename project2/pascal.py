import stdarray
import stdio
import sys

# Get n from command line, as an int.
n = (int(sys.argv[1]))

# Construct a 2D ragged list a of integers. The list must
# have n + 1 rows, with the ith (0 <= i <= n) row a[i] having
# i + 1 elements, each initialized to 1. For example, if n = 3,
# a should be initialized to [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1]].
a = []
for i in range(n + 1):
    row = [1] * (i + 1)
    a += [row]

# Fill the ragged list a using the formula for Pascal's triangle
#     a[i][j] = a[i - 1][i - 1] + a[i - 1][j]
# where 0 <= i <= n and 1 <= j < i.
for i in range(n + 1):
    for j in range(1, i):
        a[i][j] = a[i - 1][j - 1] + a[i - 1][j]

# Write out the elements of the ragged list a.
for i in range(len(a)):
    for j in range(len(a[i])):
        # If j is not the last column, write the element with a
        # space after.
        if j != len(a[i]) - 1:
            stdio.write(a[i][j])
            stdio.write(' ')
        # Otherwise, write the element with a newline after.
        else:
            stdio.writeln(a[i][j])
