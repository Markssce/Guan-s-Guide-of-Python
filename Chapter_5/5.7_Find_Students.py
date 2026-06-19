# Suppose the original exam data is a list containing exam scores of students from all classes mixed together. We now want to filter out the scores of students from a specific class. The available inputs are the mixed score list and the name list of students in the target class.

studentList=[]
studentList.append(('1200001','许枫',65,84,61))
studentList.append(('1200002','周杰',76,65,72))
studentList.append(('1200003','李丽',87,76,91))
studentList.append(('1200004','江红燕',76,90,78))

ID_studentInMyClass = ['1200001', '1200002']
Grades_studentInMyClass = []
Grades_studentInMyClass = [stu for stu in studentList if stu[0] in ID_studentInMyClass]

for stu in Grades_studentInMyClass:
    print("{}\t{}\t{}\t{}\t{}".format(stu[0],stu[1],
                                      stu[2],stu[3],stu[4]))
