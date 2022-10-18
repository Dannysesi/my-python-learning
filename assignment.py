x = []
y =[]
z =[]
print("The grade of student in 7 course in Oduduwa University: ")
a = 1
while a < 2:
    d = input("course code: ")
    x.append(d)
    b = input("course unit: ")
    y.append(b)
    grade = int(input("Your grade is: "))
    z.append(grade)
    if (grade >=70) and (grade <=100):
        print("for "+ d + " grade = A")
    elif (grade >=60) and (grade <=69):
        print("for "+ d + " grade = B")
    elif(grade >=50) and (grade <=59):
        print("for "+ d + " grade = C")
    elif(grade >=45) and (grade <=49):
        print("for "+ d + " grade = D")
    elif(grade >=40) and (grade <=44):
        print("for "+ d + " grade = E")
    elif(grade >=0) and (grade <=39):
        print("for "+ d + " grade = F")
    else:
        print("invaild grade")
    a = int(input("Do you want to compute another course grade (1/yes, 2/no) "))

else:
    print("Thank you")
    
print(x)
print(y)
print(z)

