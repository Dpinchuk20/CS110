import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Takes an integer P, a float tau, a float delta, and a sequence of JPEG
# filenames as command-line arguments; identifies the beads in each JPEG
# image using BlobFinder; and writes out (one per line, formatted with 4
# decimal places to the right of decimal point) the radial distance that
# each bead moves from one frame to the next (assuming it is no more than
# delta).
def main():

    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    frame = BlobFinder(Picture(sys.argv[4]), tau)
    prevBeads = frame.getBeads(P)
    for i in range(5, len(sys.argv)):
        frame = BlobFinder(Picture(sys.argv[i]), tau)
        currBeads = frame.getBeads(P)
        for currBead in currBeads:
            distance = float('inf')
            for prevBead in prevBeads:
                d = currBead.distanceTo(prevBead)
                if d <= delta and d < distance:
                    distance = d
            if distance != float('inf'):
                stdio.writef('%.4f\n', distance)
        stdio.writeln()
        prevBeads = currBeads


if __name__ == '__main__':
    main()
