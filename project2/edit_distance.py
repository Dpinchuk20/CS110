import stdarray
import stdio

# Read w and z.
w = stdio.readString()
z = stdio.readString()

# Create (F + 1) x (G + 1) matrix opt with elements initialized to 0, where
# F and G are lengths of w and z respectively.
opt = []
F = len(w)
G = len(z)
# create the matrix
opt = [[0 for j in range(G + 1)] for i in range(F + 1)]

# Initialize bottom row opt[F][j] (0 <= j <= G) to 2 * (G - j).
for j in range(G + 1):
    opt[F][j] = 2 * (G - j)

# Initialize right column opt[i][G] (0 <= i <= F) to 2 * (F - i).
for i in range(F + 1):
    opt[i][G] = 2 * (F - i)

# Compute the rest of opt.
for j in reversed(range(G)):
    for i in reversed(range(F)):
        # of checks if there is a penalty or not
        if w[i] == z[j]:
            opt[i][j] = min(opt[i + 1][j + 1], opt[i + 1][j] + 2,
                            opt[i][j + 1] + 2)
        else:
            opt[i][j] = min(opt[i + 1][j + 1] + 1, opt[i + 1][j] + 2,
                            opt[i][j + 1] + 2)
# Write x, y, dimensions of opt, and opt.
stdio.writeln(w)
stdio.writeln(z)
stdio.write(F + 1)
stdio.write(' ')
stdio.writeln(G + 1)
for i in range(F + 1):
    for j in range(G + 1):
        if j != G:
            stdio.writef('%3d', opt[i][j])
            stdio.write(' ')
        else:
            stdio.writef('%3d\n', opt[i][j])
