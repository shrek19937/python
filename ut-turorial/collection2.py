#!/usr/bin/env python

from collections import Counter
from bar_chart import print_ascii_bar_chart
import matplotlib.pyplot as plt

letters = Counter("mississippi")

print(letters['i'])
print(letters.most_common(2))


def count_letters(filename):
    letter_counter = Counter()
    with open(filename) as file:
        for line in file:
            line_letters = [
                char for char in line.lower() if char.isalpha()
            ]
            letter_counter.update(Counter(line_letters))
    return letter_counter

this_file = "collection2.py"
print(f"count the letters in {this_file}")
print(count_letters(this_file))


letters = "mississippimississippimississippimississippi"
print_ascii_bar_chart(letters)


sales = Counter(banana=15, tomato=4, apple=39, orange=30).most_common()
x, y = zip(*sales)
print(x)
print(y)

import matplotlib
plt.bar(x, y)
plt.show()