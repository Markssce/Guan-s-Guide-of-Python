# Define a function that, given a string instruction (sum, average, cumulative product), uses variable-length arguments to perform corresponding calculations on any number of subsequent real numbers.

# def process_(cmd, *data):
#     if cmd == "Sum":
#         ans = sum(data)
#         return ans
#     if cmd == "Aver":
#         ans = sum(data)/len(data)
#         return ans
#     else:
#         s = 1
#         for i in data:
#             s *= i
#         return s
# test = process_("Aver", 3, 3, 100, 100)
# print(test)

# Define a function that collects actual parameters into a dictionary and outputs the names and values of the actual parameters.

def keyArgFuc(**keyarg):
    for i in keyarg:
        print(i + ":" + str(keyarg[i]))
keyArgFuc(no=10, name="Mary", spec="Student", age="20")

