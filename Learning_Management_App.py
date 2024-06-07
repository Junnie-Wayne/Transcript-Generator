#This allows the student to enter his/her full name and the input is stored in the variable "studentName"
studentName = input("Enter your full name: ")

#This changes the full name entered by the student into uppercase and the result is kept in the variable "Full_Name"
Full_Name = studentName.upper()

#This allows the student to enter his/her ID and the input is stored in the variable "student_ID"
student_ID = input("Enter your ID: ")

#This allows the student to enter the name of his/her department and the input is stored in the variable "departmentName"
departmentName = input("Enter the name of your Department: ")

#This changes the name of the department entered by the student into uppercase and the result is kept in the variable "Department"
Department = departmentName.upper()

#This allows the student to enter his/her degree and the input is stored in the variable "yourDegree"
yourDegree = input("Enter your degree: ")

#This changes the degree entered by the student into uppercase and the result is kept in the variable "Degree"
Degree = yourDegree.upper()

#This allows the student to enter his/her date of birth
yourDOB = input("Enter your date of birth(DD/MM/YY): ")

#This function produces the Grade Point Total(GPT) depending on the score of the course when it is called
def yourGPT(score):
    if score >= 80:
        point = 12
    elif score >= 75:
        point = 10.5
    elif score >= 70:
        point = 9
    elif score >= 65:
        point = 7.5
    elif score >= 60:
        point = 6
    elif score >= 55:
        point = 4.5
    elif score >= 50:
        point = 3
    elif score >= 45:
        point = 1.5
    else:
        point = 0
        
    return point


def yourGrade(score):
    if score >= 80:
        grade = "A"
    elif score >= 75:
        grade = "B+"
    elif score >= 70:
        grade = "B"
    elif score >= 65:
        grade = "C+"
    elif score >= 60:
        grade = "C"
    elif score >= 55:
        grade = "D+"
    elif score >= 50:
        grade = "D"
    elif score >= 45:
        grade = "E"
    else:
        grade = "F"
        
    return grade


print("")
    

# FIRST COURSE

#Collecting information about the first course
course1_code = input("Enter the course code of the first course: ")
course1_credit = input("Enter the credit hours: ")
course1_score = input("Enter your score: ")

#Changes to upper cases, type conversion and GPT
first_course_code = course1_code.upper()
first_course_credit = int(course1_credit)
first_course_score = int(course1_score)
score1_GPT = yourGPT(first_course_score)
grade1_course = yourGrade(first_course_score)

print("")

# SECOND COURSE

#Collecting information about the second course
course2_code = input("Enter the course code of the second course: ")
course2_credit = input("Enter the credit hours: ")
course2_score = input("Enter your score: ")

#Changes to upper cases, type conversion and GPT
second_course_code = course2_code.upper()
second_course_credit = int(course2_credit)
second_course_score = int(course2_score)
score2_GPT = yourGPT(second_course_score)
grade2_course = yourGrade(second_course_score)

print("")

# THIRD COURSE

#Collecting information about the third course
course3_code = input("Enter the course code of the third course: ")
course3_credit = input("Enter the credit hours: ")
course3_score = input("Enter your score: ")

#Changes to upper cases, type conversion and GPT
third_course_code = course3_code.upper()
third_course_credit = int(course3_credit)
third_course_score = int(course3_score)
score3_GPT = yourGPT(third_course_score)
grade3_course = yourGrade(third_course_score)

print("")

# FOURTH COURSE

#Collecting information about the third course
course4_code = input("Enter the course code of the fourth course: ")
course4_credit = input("Enter the credit hours: ")
course4_score = input("Enter your score: ")

#Changes to upper cases, type conversion and GPT
fourth_course_code = course4_code.upper()
fourth_course_credit = int(course4_credit)
fourth_course_score = int(course4_score)
score4_GPT = yourGPT(fourth_course_score)
grade4_course = yourGrade(fourth_course_score)

print("")

# FIFTH COURSE

#Collecting information about the third course
course5_code = input("Enter the course code of the fifth course: ")
course5_credit = input("Enter the credit hours: ")
course5_score = input("Enter your score: ")

#Changes to upper cases, type conversion and GPT
fifth_course_code = course5_code.upper()
fifth_course_credit = int(course5_credit)
fifth_course_score = int(course5_score)
score5_GPT = yourGPT(fifth_course_score)
grade5_course = yourGrade(fifth_course_score)

# Calculating the GPA
gpa = (score1_GPT + score2_GPT + score3_GPT + score4_GPT + score5_GPT) / (first_course_credit + second_course_credit + third_course_credit + fourth_course_credit + fifth_course_credit)


print("")
print("")

################### DISPLAYING THE STUDENT RECORD ###################

print("                                        STUDENT RECORD                                             ")
print("                                ",Department,"                ")
print("                         ",Degree,"                    ")
print("Student ID:  ",student_ID)
print("Name:  ",Full_Name)
print("Date of Birth:  ",yourDOB,"                                        ","GPA:", gpa)
print("")
print("")
print("CODE        ", "CREDIT                 ", "SCORE   ", "  GRADE  ", "     GPT")
print("-----------------------------------------------------------------------------------------")
print(first_course_code,"      ", first_course_credit, "                     ", course1_score, "       ",grade1_course,"\t\t",score1_GPT)
print(second_course_code,"      ", second_course_credit, "                     ", course2_score, "       ",grade2_course,"\t\t",score2_GPT)
print(third_course_code,"      ", third_course_credit, "                     ", course3_score, "       ",grade3_course,"\t\t",score3_GPT)
print(fourth_course_code,"      ", fourth_course_credit, "                     ", course4_score, "       ",grade4_course,"\t\t",score4_GPT)
print(fifth_course_code,"      ", fifth_course_credit, "                     ", course5_score, "       ",grade5_course,"\t\t",score5_GPT)




























