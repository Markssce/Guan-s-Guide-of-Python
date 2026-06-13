from math import * # To avoid forget using math. in the terminal

# Calculate the radian from angles
angle_input = int(input("Enter the angle: "))
radian_res = sin(angle_input*pi/180)
print("sin(x)= %5.2f"%(radian_res))