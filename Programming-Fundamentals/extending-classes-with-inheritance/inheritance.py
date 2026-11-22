class Course:

    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)
    def location(self):
        print("Our head office location: Cape Town")

class OOPCourse(Course):
    def __init__(self,description ="OOP Fundamentals" ,trainer= "Mr Anon A. Mouse"):
        self.description = description
        self.trainer = trainer
        pass
    def trainer_details(self):
        print("Name of trainer:",self.trainer)
        print("Course description:",self.description)

    def show_course_id(self):
        print("Course ID number: #12345")
# Example usage:
# Create an instance of the Course class
course = Course()

# Call the contact_details method to display contact information
course.contact_details()
course_1 = OOPCourse()
print(course_1.contact_details())
print(course_1.trainer_details())
print(course_1.show_course_id())