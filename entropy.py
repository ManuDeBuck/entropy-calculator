import sys
from math import log
from copy import deepcopy

class ECalculator:

    def __init__(self, n):
        self.dict = {}
        self.total = 0
        self.n = n

    def process_element(self, character):
        self.process_char_or_substr(character, self.dict)
        self.total += 1

    def process_char_or_substr(self, char_or_substr, dict):
        if len(char_or_substr) == 1:
            char_total = dict.get(char_or_substr, 0)
            dict[char_or_substr] = char_total + 1
        else:
            char_sub_dict = dict.get(char_or_substr[0], {})
            self.process_char_or_substr(char_or_substr[1:], char_sub_dict)
            dict[char_or_substr[0]] = char_sub_dict

    def get_occurences(self):
        return self.dict

    def get_total_occurences(self):
        return self.total

    def get_entropy(self):
        probabilities = deepcopy(self.dict)
        probs = []
        self.update_probabilities(self.dict, probs)
        H = sum([ pi * log(1/pi, 2) for pi in probs])
        return H

    def update_probabilities(self, subdict, probs):
        for key in subdict:
            if isinstance(subdict.get(key), dict):
                self.update_probabilities(subdict.get(key), probs)
            else:
                subdict[key] = subdict.get(key) / self.total
                probs.append(subdict[key])


def main(filename, n):
    calculator = ECalculator(n)
    lines = "".join([line for line in open(filename, "r")])
    lines_splitted = [ el for el in [lines[i:i+n] for i in range(0, len(lines))] if len(el) == n]

    [calculator.process_element(el) for el in lines_splitted]
    print("Entropy with N = {}: {}".format(calculator.n - 1, calculator.get_entropy()))


if __name__ == "__main__":
    sys.argv.pop(0)
    if len(sys.argv) == 0 or len(sys.argv) > 2:
        raise Exception('Only one argument (filename) should be given.')
    main(sys.argv.pop(0), int(sys.argv.pop(0)) + 1 if len(sys.argv) > 0 else 1)
