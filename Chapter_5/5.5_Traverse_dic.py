# Traverse the dictionary.

student = {"name": "Tom", "age": 18, "gender": "male"}

# M1: traverse the key
for key in student:
    print(key, "->", student[key])

# M2: traverse the itmes.
for key, value in student.items():
    print(key, "->", value)