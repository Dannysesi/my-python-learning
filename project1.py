#GPA calc

#lists
classes= []
grades= []

#collects the data of class names and grades in letter form
def collect():
    i = 0
    while (i <= 6):
        className = input("Enter class Name: ")
        classes.append(className)
        i = i + 1
    

    print(classes)
    y = 0
    while (y <= 6):
        grade = input("Enter your grade for each class listed in order (letter form): ")
        grade = grade.upper()
        grades.append(grade)
        y = y + 1
    calculate()

def calculate():
    total = 0
    for element in grades:
        if element == "A":
            total = total + 5.0
        elif element == "B":
            total = total + 4.0
        elif element == "c":
            total = total + 3.0
        elif element == "D":
            total = total + 2.0
        elif element == "E":
            total = total + 1.0
    gpa = total / 7
    print(gpa)

collect()