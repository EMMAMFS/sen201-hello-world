print("STUDENT RESULT MANAGEMENT SYSTEM")
print("--------------------------------")

student_name = input("Enter student name: ")

num_courses = int(input("Enter number of courses: "))

total_score = 0

for i in range(1, num_courses + 1):
    score = float(input(f"Enter score for course {i}: "))
    total_score += score

average_score = total_score / num_courses

print("\nRESULT SUMMARY")
print("Student Name:", student_name)
print("Total Score:", total_score)
print("Average Score:", average_score)

if average_score >= 50:
    print("Status: PASS")
else:
    print("Status: FAIL")
