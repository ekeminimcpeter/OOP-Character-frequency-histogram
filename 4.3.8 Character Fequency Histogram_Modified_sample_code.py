#Modified sample code.
from os import strerror
import sys
# import sys # Not needed if you don't call sys.exit()

# Initialize 26 counters for each Latin letter.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")

# New flag to track if any alphabet character was found
found_alphabet = False 

try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            if char.isalpha():
                # Update the counter
                counters[char.lower()] += 1
                # Set the flag
                found_alphabet = True
                
    file.close()

    # --- Check the flag after processing the whole file ---
    if not found_alphabet:
        print("Nothing to display. File has no alphabet characters!")
        sys.exit()
    else:
        # Output the counters only if an alphabet was found
        for char in counters.keys():
            c = counters[char]
            if c > 0:
                print(char, '->', c)
            
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
