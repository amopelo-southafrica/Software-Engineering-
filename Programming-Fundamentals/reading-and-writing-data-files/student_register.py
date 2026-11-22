#Ask for number of students in the classroom
student_numbers = int(input("What are the number of student in your class?"))
# For each number , ask the user to enter the student ID  number 
for students in range(student_numbers):
    student_id = int(input("Enter a students ID number")) 
#Once each number has a student ID, write it in a new document 
with open('reg_form.txt', 'a') as file: 
#Write all the ID number in the document with a dotted line in the next line 
        student_list = student_id + "...\n"
print("".join(student_list))
