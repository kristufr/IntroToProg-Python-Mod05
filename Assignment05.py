# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   CCipolla, 2/14/2024, Created Script
# ------------------------------------------------------------------------------------------ #

import json  # import code from Python's json module

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.json1" # Test to get the FileNotFound error
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data

# When the program starts, read the file data into a list of
# dictionaries (students)
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)

except FileNotFoundError as e:
    print(f'\nThe file, {FILE_NAME}, does not exist.\nA blank {FILE_NAME} is being created.\n')
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    file = open(FILE_NAME, "w")
    json.dump(students,file)
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if not file.closed:
        file.close()
    print()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():  # if the first name is not all alphabetical characters
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():  # if the last name is not all alphabetical characters
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "Course": course_name}
            students.append(student_data)
            print(f"\nYou have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print("\n", "!" * 10, "  ERROR  ", "!" * 10)
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__, e.__str__(), sep='\n')
            print()
            print("No students were registered")
            print()
        except Exception as e:
            print("\n!!!!!!  ERROR!!!!!!")
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            print()
            print("No students were registered")
            print()
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        try:
            print("-" * 50)
            for student in students:
                print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["Course"]}")
            print("-" * 50)
        except KeyError as e:
            print(f"\nError found in the original file\nCheck the keys in {FILE_NAME} to ensure they match")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)

            print("\nThe following data was saved to file!")
            for student in students:
                print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["Course"]}")
            continue
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except KeyError as e:
            print(f"\nError found in the original file\nCheck the keys in {FILE_NAME} to ensure they match")
            print(f"Data saved, but the keys in {FILE_NAME} need to be cleaned up.")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        print("\nWe know you have choices when it comes to registering students.\n"
              "Thank you for choosing Assignment05.\n")
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("=" * 25)
print("Program Ended")
print("=" * 25)
