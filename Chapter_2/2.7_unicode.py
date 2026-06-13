# Input a string, display its corresponding Unicode seperately, then convert the Unicode values back to characters for verification.

list_input = input("Enter the string: ")
list_ord = []
list_verification = []
for i in list_input:
    item_ord = ord(i)
    list_ord.append(item_ord)
    list_verification.append(chr(item_ord))
    print(i,"\tord= ",ord(i), "\tverification: ", chr(ord(i)))

# for i in input("Enter the string: "):
#     print(i,"\tord= ",ord(i), "\tverification: ", chr(ord(i)))