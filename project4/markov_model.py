import stdio
import stdrandom
import sys


class MarkovModel(object):
    """
    Represents a Markov model of order k from a given text string.
    """

    def __init__(self, text, k):
        """
        Create a Markov model of order k from given text (assumed
        to have length at least k).
        """

        self._k = k
        self._st = dict()
        circ_text = text + text[:k]
        for i in range(len(circ_text) - k):
            kgram = circ_text[i:i + k]
            next_char = circ_text[i + k]
            self._st.setdefault(kgram, {})
            self._st[kgram].setdefault(next_char, 0)
            self._st[kgram][next_char] += 1

    def order(self):
        """
        Return order of Markov model.
        """

        return self._k

    def kgram_freq(self, kgram):
        """
        Return number of occurrences of kgram in text.
        """

        if kgram not in self._st:
            return 0
        return sum(self._st[kgram].values())

    def char_freq(self, kgram, c):
        """
        Return number of times character c follows kgram.
        """

        if kgram not in self._st or c not in self._st[kgram]:
            return 0
        return self._st[kgram][c]

    def rand(self, kgram):
        """
        Return a random character following kgram.
        """

        a = list(self._st[kgram].values())
        b = list(self._st[kgram].keys())
        for i in range(len(a)):
            a[i] = a[i] / float(sum(a))
        d = stdrandom.discrete(a)
        return b[d]

    def gen(self, kgram, T):
        """
        Generate and return a string of length T by simulating a trajectory
        through the correspondng Markov chain. The first k (<= T) characters
        of the generated string is the argument kgram.
        """

        text = kgram
        for i in range(T - self._k):
            text += self.rand(kgram)
            kgram = text[-self._k:]
        return text

    def replace_unknown(self, corrupted):
        """
        Replace unknown characters (~) in corrupted with most probablenb
        characters, and return that string.
        """

        # Return the index of the maximum element in the given list a.
        def argmax(a):
            return a.index(max(a))

        original = ''
        for i in range(len(corrupted)):
            if corrupted[i] == '~':
                k_before = corrupted[i - self._k: i]
                k_after = corrupted[i + 1: i + 1 + self._k]
                probs = []
                next_chars = list(self._st[k_before].keys())
                for next_char in next_chars:
                    n = k_before + next_char + k_after
                    p = 1.0
                    for i in range(self._k + 1):
                        kgram = n[i: i + self._k]
                        char = n[i + self._k]
                        if kgram not in self._st or char \
                           not in self._st[kgram]:
                            p = 0.0
                            break
                        else:
                            p *= self.char_freq(kgram, char) /\
                                self.kgram_freq(kgram)
                    probs.append(p)
                original += next_chars[argmax(probs)]
            else:
                original += corrupted[i]
        return original


def _main():
    """
    Test client [DO NOT EDIT].
    """

    text, k = sys.argv[1], int(sys.argv[2])
    model = MarkovModel(text, k)
    a = []
    while not stdio.isEmpty():
        kgram = stdio.readString()
        char = stdio.readString()
        a.append((kgram.replace("-", " "), char.replace("-", " ")))
    for kgram, char in a:
        if char == ' ':
            stdio.writef('freq(%s) = %s\n', kgram, model.kgram_freq(kgram))
        else:
            stdio.writef('freq(%s, %s) = %s\n', kgram, char,
                         model.char_freq(kgram, char))


if __name__ == '__main__':
    _main()
