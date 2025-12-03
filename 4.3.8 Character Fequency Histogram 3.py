#McCoy McPeter
#Date: 27-10-2025
#Rev: 3

from os import strerror
import os
from collections import Counter
import sys

# Get user name of file to copy
srcname = input("Enter the source file name: ")

# If user didn't include ".txt", add it automatically
if not os.path.splitext(srcname)[1]:  
    srcname += ".txt"

try:
    with open(srcname, 'rt') as src:
        counts = Counter()
        has_content = False

        for line in src:
            has_content = True
            counts.update(ch for ch in line.lower() if ch.isalpha())

    if not has_content:
        print("Nothing to display. File has no content!")
        sys.exit()

    # Sort alphabetically and print
    for letter in sorted(counts):
        print(f"{letter} -> {counts[letter]}")

except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    
    			
    


