# entropy-calculcator

A simple Python script to compute the (Shannon)-entropy of a text file with memory N.

When N = 0 the entropy is calculated without memory.
When N > 0 the entropy is calculated based on the previous N characters.

## Usage

```bash
$ python3 entropy path/to/inputfile N
```

## Example usage
```bash
$ python3 entropy.py input/input.txt 5
> Entropy with N = 5: 8.716007696474326
```
