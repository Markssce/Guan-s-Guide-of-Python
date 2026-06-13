# Use the iterative method to find the cube root of a, where a ranges from 1 to 10.

cubeRoot = 1 # Any number(regular)
for a in range(1, 11):
    while 1:
        cubeRoot_origin = cubeRoot
        cubeRoot = 2/3 * cubeRoot + a / (3*cubeRoot**2)
        if abs(cubeRoot_origin-cubeRoot)<1e-5:
            break
    print("The cube root of {0:d} is {1:5.4f}".format(a, cubeRoot))
