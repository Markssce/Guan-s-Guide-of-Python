# Program to calculate the factorial n!

def factorial(n):
    if n == 1:
        return 1
    else: 
        return n*factorial(n-1)

print("The n! is ",factorial(int(input("Enter n: "))))