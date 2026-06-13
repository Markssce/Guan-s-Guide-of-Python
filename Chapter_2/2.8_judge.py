# Enter the score, judge if excellent(90~100 for excellent grade)
mark = int(input("Enter the score: "))
print(90<=mark and mark<=100)

# Enter three sides of a triangle and judge whether they can form a valid triangle.
a,b,c = eval(input("Enter a, b, c: ")) # The eval() is great, isn't it? :)
print(a+b>c and a+c>b and b+c > a)

'''Select outstanding students. The criteria for selection are as follows: the student's age is less than 19, 
    the total score of three courses exceeds 285 points, and at least one of the three subjects scores 100.
'''
age = int(input("Age: "))
score_a, score_b, score_c = eval(input("Score of class A, B, C: "))
score_total = score_a + score_b + score_c
print(age < 19 and score_total > 285 and (score_a == 100 or score_b == 100 or score_c == 100))
