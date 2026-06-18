# Count the occurrences of each character in string s.

def charFreq(s):
    chars = list(set(s))
    chars.sort()
    freq = []
    for char in chars:
        v = s.count(char)
        freq = freq + [v]
    return chars, freq

str1 = input("Enter string: ")
charList, freqList = charFreq(str1)
print(charList)
print(freqList)