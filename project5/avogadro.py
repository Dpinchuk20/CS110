import math
import stdio


# Reads in the displacements produced by bead_tracker.py from standard
# input; computes an estimate of Boltzmann's constant and Avogadro's number;
# and writes those estimates to standard output.
def main():
    n = 0
    var = 0
    while not stdio.isEmpty():
        z = stdio.readFloat() * 0.175 * 10 ** -6
        var += z * z
        n += 1
    var = var / (2 * n)
    eta = 9.135 * 10 ** -4
    rho = 0.5 * 10 ** -6
    T = 297
    R = 8.31457
    k = 6 * math.pi * var * eta * rho / T
    N_A = R / k
    stdio.writef('Boltzman = %e\nAvogadro = %e\n', k, N_A)


if __name__ == '__main__':
    main()
