x = []
caltimes=0
totalcal=0
totalcredit=0

course=int(input("Enter number of course: "))
for i in range(0,course):
    y=input("Enter course_code: ")
    x=int(input("Enter course unit: "))
    g=int(input("Enter grade: "))

    if x==x:

        caltimes= x * g
        totalcredit= totalcredit + x
        totalcal= totalcal + caltimes

gpa= totalcal/totalcredit

print(totalcredit)
print(totalcal)
print("GPA:" + str(gpa))


 