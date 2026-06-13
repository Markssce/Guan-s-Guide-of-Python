# Solusion 1: reverse the string.
num_input = str(input("Enter a three-digit number: "))
print("Result is %d"%(int(num_input[::-1])))

# Solusion 2: Calculate the units,tens and hundreds:
num_input = int(num_input)
hundreds_res = num_input // 100
tens_res = (num_input//10) % 10
units_res = num_input % 10
print("Result is %d"%(100*units_res + 10*tens_res + hundreds_res))