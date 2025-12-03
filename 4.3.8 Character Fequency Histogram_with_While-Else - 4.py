#Code using while–else
#Code modified and corrected by ChatGPT
#Rev 4


from os import strerror
import os
from collections import Counter
import sys

srcname = input("Enter the source file name: ")

# Append ".txt" if missing
if not os.path.splitext(srcname)[1]:
    srcname += ".txt"

try:
    src = open(srcname, 'rt')

    counts = Counter()
    text_line = src.readline()

    # Loop will break immediately when the first real content is found
    while text_line != '':
        if text_line.strip():  # this line contains something (not empty)
            break
        text_line = src.readline()

    else:
        # Loop ended WITHOUT a break → file had no content
        print("Nothing to display. File has no content!")
        sys.exit()

    # If we reach this point → FIRST non-empty line was already read
    # Count letters in this line
    counts.update(ch for ch in text_line.lower() if ch.isalpha())

    # Continue reading the rest of the file normally
    for line in src:
        counts.update(ch for ch in line.lower() if ch.isalpha())

    src.close()

    # Print results sorted
    for letter in sorted(counts):
        print(f"{letter} -> {counts[letter]}")

except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
