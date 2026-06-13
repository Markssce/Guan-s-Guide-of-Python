# Generate the multiplication table from 1 to 9

# for i in range(1, 10):
#     for j in range(1, 10):
#         print("{}*{}={:2d}".format(i, j, i*j), end=" ")
#     print()


# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("{}*{}={:2d}".format(i, j, i*j), end=" ")
#     print()


for i in range(1, 10):
    for j in range(i, 10):
        print(" "*7+"{}*{}={:2d}".format(i, j, i*j), end=" ")
    print()



