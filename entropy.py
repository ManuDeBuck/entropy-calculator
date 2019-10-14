import sys
from math import log
from copy import deepcopy
from PIL import Image


class ECalculator:

    def __init__(self, n):
        self.dict = {}
        self.dict_min = {}
        self.total = 0
        self.n = n

    def process_element(self, character):
        self.process_char_or_substr(character, self.dict)
        if self.n > 1:
            self.process_char_or_substr(character[:-1], self.dict_min)
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
        probs = {}
        probs_min = {}
        self.update_probabilities(self.dict, probs, "")
        if self.n > 1:
            self.update_probabilities(self.dict_min, probs_min, "")
            return sum([-probs[key] * log(probs[key] / probs_min[key[:-1]], 2) for key in probs])
        else:
            return sum([-probs[key] * log(probs[key], 2) for key in probs])

    def update_probabilities(self, subdict, probs, str):
        for key in subdict:
            if isinstance(subdict.get(key), dict):
                str += key
                self.update_probabilities(subdict.get(key), probs, str)
                str = str[:-1]
            else:
                str += key
                probs[str] = subdict.get(key) / self.total
                str = str[:-1]


def main(filename, image, n):
    calculator = ECalculator(n)
    if image.lower() == "true":
        image = Image.open(filename, 'r')
        pixels = "".join(map(str, list(image.getdata())))
        elements_splitted = [el for el in [pixels[i:i + n] for i in range(0, len(pixels))] if len(el) == n]
    else:
        lines = "".join([line for line in open(filename, "r")])
        elements_splitted = [el for el in [lines[i:i + n] for i in range(0, len(lines))] if len(el) == n]
    [calculator.process_element(el) for el in elements_splitted]
    print("Entropy with N = {}: {}".format(calculator.n - 1, calculator.get_entropy()))


if __name__ == "__main__":
    sys.argv.pop(0)
    if len(sys.argv) == 0 or len(sys.argv) > 3:
        raise Exception('The amount of arguments given is not correct.')
    main(sys.argv.pop(0), sys.argv.pop(0), int(sys.argv.pop(0)) + 1 if len(sys.argv) > 0 else 1)
