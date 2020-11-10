from com.abc.lib.student_ops import get_details, get_grade

n1 = 'mehul'
g1 = 'm'
r1 = 10
m1 = 90

n2 = 'jane'
g2 = 'f'
r2 = 13
m2 = 67

print(get_details(name=n1, gender=g1, roll=r1, marks=m1))
print(get_details(name=n2, gender=g2, roll=r2, marks=m2))

print(get_grade(marks=m1))
print(get_grade(marks=m2))