class_score = float(input("Enter the class score: "))

A_score = 90
B_score = 80
C_score = 70
D_score = 60

if class_score >= A_score:
    grade = 'A'
elif class_score >= B_score:
    grade = 'B'
elif class_score >= C_score:
    grade = 'C'
elif class_score >= D_score:
    grade = 'D'
else:
    grade = 'F'

print("Letter Grade:", grade)