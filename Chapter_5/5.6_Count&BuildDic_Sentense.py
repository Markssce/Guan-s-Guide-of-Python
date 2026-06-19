# Function that counts the occurrences of each character in an English sentence, generates a dictionary with characters as keys and their occurrence counts as values, and returns the dictionary.

def charFreq(s):
    chars = list(set(s))
    chars.sort()

    freq = {}
    for char in chars:
        times = s.count(char)
        freq[char] = times
    return freq

str1 = input("Enter the string: ")
print(charFreq(str1))