import stdio
import sys
from markov_model import MarkovModel


def main():
    k = int(sys.argv[1])
    s = str(sys.argv[2])
    text = sys.stdin.read()
    model = MarkovModel(text, k)
    stdio.writeln(model.replace_unknown(s))


if __name__ == '__main__':
    main()

