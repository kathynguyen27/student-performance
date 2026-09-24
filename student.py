#Kathy Nguyen
#PM
#Student Performance Analyzer

#Program introduction
print("=================================")
print("STUDENT PERFORMANCE")
print("=================================")

#collecting info
name = input("What is your name?: ")
grade = int(input("What grade are you in?: "))
assignment_avg = float(input("What is your assignment average?: "))
quiz_avg = float(input("What is your quiz average?: "))
test_avg = float(input("What is your test average?: "))
attendance = float(input("What is your attendance percentage?: "))
missing_assignments = int(input("How many missing assignments do you have?: "))

#functions
overall_grade = 0
def calculate_grade(assignment_avg, quiz_avg, test_avg):
    return (assignment_avg*0.3) + (quiz_avg*0.3) + (test_avg*0.4)

result = overall_grade
overall_grade = calculate_grade(assignment_avg, quiz_avg, test_avg)


def letter_grade(overall_grade):
    if overall_grade >= 90:
        return "A"
    elif 80 <= overall_grade <= 89.99:
        return "B"
    elif 70 <= overall_grade <= 79.99:
        return "C"
    elif 60 <= overall_grade <= 69.99:
        return "D"
    else:
        return "F"

letter_grade = letter_grade(overall_grade)

def attendance_status(attendance):
    if attendance >= 95:
        return "Attendance Status: Excellent attendance"
    elif 90 <= attendance <= 94.99:
        return "Attendnace Status: Good attendance"
    elif 80 <= attendance <= 89.99:
        return "Attendance Status: Attendance warning"
    else:
        return "Attendance Status: Poor Attendance"
attendance_status = attendance_status(overall_grade)

def assignment_status(missing_assignments):
    if missing_assignments == 0:
        return "Missing Assignment Status: Excellent"
    elif 1 <= missing_assignments <= 2:
        return "Missing Assignment Status: Good"
    elif 3 <= missing_assignments <= 4:
        return "Missing Assignment Status: Warning"
    else:
        return "Missing Assignment Status: Critical"
assignment_status = assignment_status(missing_assignments)

def check_eligibility(overall_grade, attendance, missing_assignments):
    if overall_grade >= 70:
        if attendance >= 90:
            if missing_assignments <= 2:
                return "Academic Eligibility: ELIGIBLE | Student passed all 3 requirements"
            else:
                return "Academic Eligibility: NOT ELIGIBLE | Reason: Too many missing assignments"
        else:
            return "Academic Eligibility: NOT ELIGIBLE | Reason: Attendance is too low"
    else:
        return "Academic Eligibility: NOT ELIGIBLE | Reason: Overall grade is too low"

eligibility = check_eligibility(overall_grade, attendance, missing_assignments)

def check_high_honors(overall_grade, attendance, missing_assignments):
    if overall_grade >= 90:
        if attendance >= 95:
            if missing_assignments == 0:
                return "High Honors: YES"
            else:
                return "High Honors: NO | Reason: Student has missing assignments"
        else:
            return "High Honors: NO | Reason: Attendance requirement not met"
    else:
        return "High Honors: NO | Reason: Grade requirement not met"

high_honors = check_high_honors(overall_grade, attendance, missing_assignments)

def check_good_standing(overall_grade, attendance):
    if overall_grade >= 70 and attendance >= 90:
        return "Good Standing: YES"
    else:
        return "Good Standing: NO"

standing = check_good_standing(overall_grade, attendance)

def check_support(overall_grade, attendance):
    if overall_grade < 70 or attendance < 80:
        return "Additional Support: RECOMMENDED"
    else:
        return "Additional Support: NOT NEEDED"

support = check_support(overall_grade, attendance)

#login check
username = input("Enter username: ")
pin = int(input("Enter PIN: "))

def program(username, pin):
    if username == "student":
        if pin == 1234:
            return "Login Successful!"
        else:
            return "Login Failed: Incorrect PIN"
    else:
        return "Login failed: Incorrect Username"

program_status = program(username, pin)

def grade_level_message(grade):
    if grade == 9:
        return "Freshman year - Welcome to your freshman year!"
    elif grade == 10:
        return "Sophomore year - Keep building skills!"
    elif grade == 11:
        return "Junior year - Keep pushing!"
    elif grade == 12:
        return "Senior year - Finish strong!"
    else:
        return "Invalid grade level"

message = grade_level_message(grade)

def strongest_category(assignment_avg, quiz_avg, test_avg):
    if assignment_avg > quiz_avg > test_avg or assignment_avg > test_avg > quiz_avg:
        return "Strongest Category: Assignments"
    elif quiz_avg > assignment_avg > test_avg or quiz_avg > test_avg > assignment_avg:
        return "Strongest Category: Quizzes"
    elif test_avg > assignment_avg > quiz_avg or test_avg > quiz_avg > assignment_avg:
        return "Strongest Category: Tests"
strong = strongest_category(assignment_avg, quiz_avg, test_avg)

def check_advanced_status(overall_grade, attendance, missing_assignments):
    if overall_grade >= 90 and attendance >= 95 or overall_grade >= 85 and missing_assignments == 0:
        return "OUTSTANDING STATUS"
    else:
        return "STANDARD STUDENT STATUS"

adv_status = check_advanced_status(overall_grade, attendance, missing_assignments)


#the final result
print("==============================")
print(" STUDENT ANALYSIS ")
print("==============================")
print(" ")
print(program_status)
print(" ")
print("Student: ", name)
print("Grade level ", grade)
print(message)
print(" ")
print("AVERAGES")
print("-----------------------------")
print("Assignment Average: ", assignment_avg)
print("Quiz Average: ", quiz_avg)
print("Test Average: ", test_avg)
print(" ")

print("GRADES AND ATTENDANCE")
print("-----------------------------")
#got it from the disneyland assignment but this is just to shorten the amt of decimals
print("Overall grade:", f"{overall_grade:.2f}")
print("Letter Grade:", letter_grade)
print("Missing Assignments: ", missing_assignments)
print(support)
print("Attendance %: ", attendance)
print(attendance_status)
print(" ")

print("MISCELLANEOUS")
print("-------------------------")
print(eligibility)
print(strong)
print(high_honors)
print(standing)
print("Advanced Status: ", adv_status)
