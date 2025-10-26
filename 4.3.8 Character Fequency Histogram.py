#McCoy McPeter
#Date: 25-10-2025
#Rev: 0

from os import strerror
import os
 
# Get user name of file to copy
srcname = input("Enter the source file name: ")

# If user didn't include ".txt", add it automatically
if not os.path.splitext(srcname)[1]:  
    srcname += ".txt"

#Create an empty dictionary for key-value pair counting
counts = {}

try:
    src = open(srcname, 'rt') #open source file object
    text_line = src.readline().lower()  #Read lines contents from source file, normalize case (lowercase) and return as string

    while text_line != '':

        # Count letters
        for ch in text_line:
            if ch.isalpha():  # count only letters
                counts[ch] = counts.get(ch, 0) + 1 #update the number of times each character appears
        text_line = src.readline().lower()
    
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)			
    
# Sort alphabetically and print
for letter in sorted(counts):
    print(f"{letter} --> {counts[letter]}")
src.close()
