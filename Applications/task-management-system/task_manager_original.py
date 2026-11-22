from datetime import datetime
import sys
###========================================================================================================Task manager========================================================================================================###



                    #====================================================Register user ====================================================#

def register_user():
    print("Register user selected")

    #---Takes a login details from the user 
    while True:
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")
        if not new_username or not new_password:
            print("Username and password cannot be empty.")
            continue
        if len(new_username) > 20 or len(new_password) > 20:
            print("Username or password too long (max 20 characters).")
            continue

        if "," in new_username or "," in new_password:
            print("Username and password cannot contain commas.")
            continue


        duplicate_found = False
        #---Checks if it already exists within the registration list 
        try:
            with open("user.txt", "r") as user_file:
                for line in user_file:
                    existing_username = line.strip().split(",")[0]
                    if existing_username == new_username:
                        duplicate_found = True
                        break
        except FileNotFoundError:
            open("user.txt", "w").close()

        if duplicate_found:
            print("Username already exists. Try again.")
            continue

        confirm_username = input("Confirm username: ")
        confirm_password = input("Confirm password: ")

        #---Stores user details in a file for logins
        if new_username == confirm_username and \
        new_password == confirm_password:
            with open("user.txt", "a") as user_file:
                user_file.write(f"{new_username},{new_password}\n")
            print("User registered successfully.")
            break
        else:
            print("Confirmation does not match. Try again.")

                #====================================================Add task====================================================#

def add_task():
    print("Add task selected")
    assigned_person = input("Assign task to: ")
    title_of_task = input("Task title: ")
    description_of_task = input("Task description: ")
    due_date = input("Due date (YYYY-MM-DD): ")
    complete = "No"

    #---Checks if the information provided is accurately presented [line 68-83]
    if not assigned_person or not title_of_task or\
    not description_of_task or not due_date:
        print("All fields are required.")
        return
    if "," in assigned_person or "," in title_of_task\
    or "," in description_of_task:
        print("Fields cannot contain commas.")
    try:
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return
    today = datetime.today()
    if due_date_obj.date() < today.date():
        print("Due date cannot be in the past.")
        return
    current_date = datetime.today().strftime("%Y-%m-%d")

    #---Stores the task in the file to be used later [line 86-95]
    try:
        with open("tasks.txt", "a") as tasks_file:
            tasks_file.write(
            f"{assigned_person},{title_of_task},"
            f"{description_of_task},\
            {current_date},{due_date},{complete}\n"
        )
        print(f"{title_of_task} added successfully.")
        return
    except IOError:
        print("Error writing to file. Try again.")
           

                #====================================================View all tasks ====================================================#

def view_all_tasks():
    print("View all selected")
    with open("tasks.txt", "r") as task_file:
        for task in task_file:
            user_entry = task.strip()
            name, title, description,current,\
            due,status = user_entry.split(",")
            print("---" * 10)
            print(
            f"Assigned person:\t{name}\n"
            f"Title of task:\t\t{ title}\n"
            f"Description:\t\t{description}\n"
            f"Current date:\t\t{current}\n"
            f"Due date:\t\t{due}\n"
            f"Task complete:\t\t{status}\n"
            )
            print("---" * 10)


            #====================================================View my tasks====================================================#                                        

def view_my_tasks():
    print("View mine selected")

    task_viewer = input("Enter your username that you " \
    "provided during your login section: ").strip()
    if not task_viewer:
        print("Username cannot be empty.")
    else:   
        with open("tasks.txt", "r") as task_file:
            tasks = task_file.readlines()
            for i, task in enumerate(tasks):
                person,title,instructions,\
                date,due,done = task.strip().split(",")
                if person == task_viewer:
                    print("---" * 10)
                    print(f"Task number: {i}")
                    print(
                        f"Assigned to: {person}\n"
                        f"Title: {title}\n"
                        f"Description: {instructions}\n"
                        f"Date assigned: {date}\n"
                        f"Due date: {due}\n"
                        f"Complete: {done}\n"
                        )
                    print("---" * 10)
    #---Allows the user to choose which task they would to operate on  [line 145 -150]
    print(
        "According to the tasks you have been assigned to,\n " \
        "please enter the task number where you would like to operate changes" \
        "to or enter -1 to go back to the menu"
        )
    try:
        picked_task = int(input("Enter the number: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if picked_task == -1:
        return
    else:
        try:

    #---Allows the user to mark as complete or edit the task [line 159 - 212]
            print("Would you like to \n" \
            "a - mark the task as complete?\n"
            "b - edit the task\n ")
            changes = input("Enter a or b:")
        except ValueError:
            print("Invalid, please enter a number.")
 
        if changes == "a":
            try:
                with open("tasks.txt", "r") as task_file:
                    tasks = task_file.readlines()
            except FileNotFoundError:
                print("No tasks found yet.")
                return
            for i, task in enumerate(tasks):
                person, title, instructions, start_date\
                ,due_date,is_complete = task.strip().split(",")
                if person == task_viewer:
                    yes_or_no  = "Yes"
                    tasks[i] = f"{person},{title},\
                    {instructions},{start_date},{due_date},{yes_or_no}\n"                           
            with open("tasks.txt", "w") as task_file:
                task_file.writelines(tasks)
            print(f'Task {i} has been marked as complete')

        #--Allows the user to edit the task 
        elif changes == "b":
            print(
            "What would you like to edit?:\n" \
            "1. Assigned person\n" \
            "2. Title of the task\n" \
            "3. Task Description\n" \
            "4. Start date\n" \
            "5. Due date\n")
            edit = input("Choose from 1- 4:\n")
            print("Enter the new update information according to what you selected")
            new_info = input("Enter the updated information:")
            with open("tasks.txt", "r") as task_file:
                tasks = task_file.readlines()
                for i, task in enumerate(tasks):
                    person, title, instructions, start_date,\
                    due_date,is_complete = task.strip().split(",")
                    if i == picked_task :
                            if is_complete == "Yes":
                                print("Task already completed , cannot edit.")
                            if edit == "1":
                                tasks[i] = f"{new_info},{title},\
                                {instructions},{start_date},{due_date},{is_complete}\n"
                                print(f'{person} has been updated to {new_info}')
                            elif edit == "2":
                                tasks[i] = f"{person},{new_info},\
                                {instructions},{start_date},{due_date},{is_complete}\n"
                                print(f'{title} has been updated to {new_info}')
                            elif edit == "3":
                                tasks[i] = f"{person},{title},\
                                {new_info},{start_date},{due_date},{is_complete}\n"
                                print(f'{instructions} has been updated to {new_info}')
                            elif edit == "4":
                                tasks[i] = f"{person},{title},\
                                {instructions},{start_date},{new_info},{is_complete}\n"
                                print(f'{due_date} has been updated to {new_info}')
            with open("tasks.txt", "w") as task_file:
                task_file.writelines(tasks)                   
                                
                #====================================================Delete tasks====================================================#

def delete_task():
    print("Delete selected")
    with open("tasks.txt", "r") as task_file:
        name_verification = input("Please enter your username:")
        tasks = task_file.readlines()
        for i,task in enumerate(tasks):
            name, title, description,\
            current,due,status = task.strip().split(",")
            if name == name_verification:
                print("---" * 10)
                print(
                f"Task:\t{i}\n"
                f"Assigned person:\t{name}\n"
                f"Title of task:\t\t{title}\n"
                f"Description:\t\t{description}\n"
                )
                print("---" * 10)
            try:
                choice = int(input("Enter task number to delete: "))
            except ValueError:
                print("Please enter a valid number.")
                return
            tasks.pop(choice)
        with open("tasks.txt", "w") as task_file:
            task_file.writelines(tasks)
            print("Task deleted successfully.")
                
    

                #====================================================Generate report ====================================================# 

def generate_reports():
    print("Generate reports selected")

    with open("tasks.txt", "r") as f:
        tasks = f.readlines()

    #---Generating the statistics to store in a report [line 247 - 262]
    total_tasks = len(tasks)
    completed = 0
    incomplete = 0
    overdue = 0
    today = datetime.today()
    user_of_data = input("Please enter your name to get your stats:")

    for task in tasks:
        name, title, description,\
        current,due,status = task.strip().split(",")
        due_date = datetime.strptime(due, "%Y-%m-%d")
        if name == user_of_data:           
            if status== "Yes":
                completed += 1
            else:
                incomplete += 1
            if due_date < today:
                overdue += 1
    incomplete_percent = (incomplete / total_tasks) * 100 
    overdue_percent = (overdue / total_tasks) * 100 
    
    #---Stores the statistics in file [line 266 - 278]
    try:
        with open("user_overview.txt", "w") as report:
            report.write(
                f"\nTASK OVERVIEW\n"
                f"Total tasks:\t {total_tasks}\n"
                f"Completed: \t {completed}\n"
                f"Incomplete: \t  {incomplete}\n"
                f"Overdue: \t {overdue}\n"
                f"Incomplete stat: \t {incomplete_percent}%\n"
                f"Overdue stat:\t {overdue_percent}%\n"
                )
    except IOError:
        print("Error generating report.")
    
    #====================================================Statistics ====================================================# 
def statistics():
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()

    #---Generating the statistics to store in a report [line 247 - 262]
        total_tasks = len(tasks)
        completed = 0
        incomplete = 0
        overdue = 0
        today = datetime.today()
        user_of_data = input("Please enter your name to get your stats:")

        for task in tasks:
            name, title, description,\
            current,due,status = task.strip().split(",")
            due_date = datetime.strptime(due, "%Y-%m-%d")
            if name == user_of_data:           
                if status== "Yes":
                    completed += 1
                else:
                    incomplete += 1
                if due_date < today:
                    overdue += 1
        incomplete_percent = (incomplete / total_tasks) * 100 
        overdue_percent = (overdue / total_tasks) * 100 
    print("Report generated. Here is a preview:\n")
    print(f'Total tasks: \t\t{total_tasks}\n'
        f'Total completed tasks: \t\t{completed}\n'
        f'Total incomplete task: \t\t{incomplete}\n'
        f'Total overdue task: \t\t{overdue}\n')       
                #====================================================View completed tasks====================================================#

def view_completed():
    print("View completed tasks ")
    with open("tasks.txt", "r") as task_file:
        tasks = task_file.readlines()
        for each_task in tasks:
            name, title, description,due_task,\
            current_date,the_status = each_task.strip().split(",")
            if the_status == "Yes":
                print("---" * 10)
                print(
                f"Assigned person:\t{name}\n"
                f"Title of task:\t\t{title}\n"
                f"Description:\t\t{description}\n"
                )
                print("---" * 10)
               
                #====================================================Exit task manager====================================================# 

def exit_program():
    choice = input("Enter 'out' to exist").strip().lower()
    if choice == "out":
        print("Goodbye.")
        sys.exit()

                    ###====================================================###End of a task manager###====================================================###



                        ###====================================================User login ====================================================###

print("\n" + "="*60)
print("Hi Im TaskFlow\n"
"I am designed to help you stay organized, focused, and in control of your work."
"\nAdd tasks, track progress, and build " \
"momentum — one step at a time. [Developed by Amogelang Pelo]")
print("="*60)

admin_username = "admin"
admin_password = "adm1n"

MAX_ATTEMPTS = 3
attempts = 0

it_is_admin  = False
it_is_user = False

while attempts < MAX_ATTEMPTS:

    #---Gets the user logins and verify [line 341 - 377]
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if not username or not password:
        print("Username and password cannot be empty.\n")
        continue
    if len(username) > 20 or len(password) > 20:
        print("Input too long.\n")
        continue

 
    if username == admin_username and password == admin_password:
        print("Welcome admin, Login successful.\n")
        it_is_admin = True
        break

    user_found = False
    with open("user.txt", "r") as user_file:
        users = user_file.readlines()
    for user in users:
        name, user_password = user.strip().split(",")
        if name == username and user_password == password:
            print("Welcome user, Login successful.\n")
            it_is_user = True
            user_found = True
            break
    if user_found:
        break
    else:
        attempts += 1
        print(f"Invalid credentials. Attempts remaining: \t{MAX_ATTEMPTS - attempts}")

else:
    print("Too many failed attempts. Exiting system.")
    sys.exit()
  ###========================================================================================================#End of User login and registration#========================================================================================================-###
  
                    ###====================================================Menu====================================================###
while True:

    #---Admin menu[line 382 - 394]
    if it_is_admin:
        print("\n" + "="*60)
        print("TASKFLOW MAIN MENU")
        print("="*60)
        menu = input(
            "\nAdmin Menu:\n"
            "r  - register user\n"
            "a  - add task\n"
            "va - view all tasks\n"
            "vc - view completed tasks\n"
            "vm - view my tasks\n"
            "del - delete task\n"
            "gr - generate reports\n"
            "e  - exit\n"
            "Select option: "
        ).lower()

    #---Presents User menu if it is user [line 397 - 405]
    elif it_is_user:
        print("\n" + "="*60)
        print("TASKFLOW MAIN MENU")
        print("="*60)
        menu = input(
            "\nUser Menu:\n"
            "a  - add task\n"
            "va - view all tasks\n"
            "vm - view my tasks\n"
            "e  - exit\n"
            "ds - display statistics"
            "Select option: "
        ).lower()

    #---Menu with functions[line 407 - 431]
    if menu == "r" and it_is_admin:
        register_user()

    elif menu == "a":
        add_task()

    elif menu == "va":
        view_all_tasks()

    elif menu == "vm":
        view_my_tasks()

    elif menu == "vc" and it_is_admin:
        view_completed()

    elif menu == "del" and it_is_admin:
        delete_task()

    elif menu == "gr" and it_is_admin:
        generate_reports()

    elif menu == "ds":
        statistics()

    elif menu == "e":
        exit_program()
        break

    else:
        print("Invalid option.")

                    ##====================================================###End of a menu ###====================================================##
