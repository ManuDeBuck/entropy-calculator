import sys
from math import log
from copy import deepcopy

class ECalculator:

    def __init__(self, n):
        self.dict = {}
        self.total = 0
        self.n = n

    def process_element(self, character):
        char_total = self.dict.get(character, 0)
        self.dict[character] = char_total + 1

        self.total += 1

    def get_occurences(self):
        return self.dict

    def get_total_occurences(self):
        return self.total

    def get_entropy(self):
        probabilities = deepcopy(self.dict)
        [probabilities.update({ch: probabilities[ch] / self.total}) for ch in probabilities.keys()]
        if self.n is not None and self.n > 0:
            H = None
        else:
            H = sum([ pi * log(1/pi, 2) for pi in probabilities.values()])
        return H


def main(filename, n=None):
    calculator = ECalculator(n)
    lines = [line for line in open(filename, "r")]
    [[calculator.process_element(ch) for ch in line] for line in lines]
    print(calculator.get_occurences(), calculator.get_total_occurences())
    print(calculator.get_entropy())


if __name__ == "__main__":
    sys.argv.pop(0)
    if len(sys.argv) == 0 or len(sys.argv) > 2:
        raise Exception('Only one argument (filename) should be given.')
    main(sys.argv.pop(0), int(sys.argv.pop(0)) if len(sys.argv) > 0 else None)
