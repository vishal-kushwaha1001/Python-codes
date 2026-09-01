def char_frequency(seq):
    freq = {}                 # Dictionary to store frequency

    for ch in seq:              # Loop through each character
        if ch in freq:
            freq[ch] += 1     # Increment count if character exists
        else:
            freq[ch] = 1      # Add character with count 1

    return freq               # Return the dictionary


# Main program
string = input("Enter a string: ")
result = char_frequency(string)
print("Character Frequency:", result)
