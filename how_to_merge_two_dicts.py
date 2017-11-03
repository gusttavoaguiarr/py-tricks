# Merging two dicts in Python 3.5+ with a single expression

# How to merge two dicts
# in Python 3.5+

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}

print(z)
