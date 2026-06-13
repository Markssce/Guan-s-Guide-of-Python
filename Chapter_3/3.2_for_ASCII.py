# Print the printable characters and their ASCII codes in a tabular format, with 7 characters printed per line.
# In ASCII codes, characters from space to tilde (~) are printable, while the rest are non-printable control characters. Printable characters correspond to ASCII values ranging from 32 to 126, and the chr() function can be used to retrieve the character matching a given code value.

n = 0
for ascii in range(32, 127):
    print("%s = %d"%(chr(ascii), ascii),end = '\t')
    n+=1
    if n%7 == 0:
        print()

