# COMP 3005 - Assignment 3

import psycopg2
from datetime import datetime

# Connect to the PostgreSQL database
def connectToDatabase():
    try:
        # Connect to a specific database in the PostgreSQL server
        connection = psycopg2.connect(
            host="134.117.133.250",
            database="students",
            user="postgres",
            password="comp3005!",
            port="5432"
        )
        return connection

    except psycopg2.Error as error:
        print("Database connection failed:", error)
        return None

# 1. Display all students
def getAllStudents():
    connection = connectToDatabase()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        # Collect all student records from the database
        cursor.execute("SELECT student_id, first_name, last_name, email, enrollment_date " \
            "FROM students " \
            "ORDER BY student_id;")

        students = cursor.fetchall()

        if not students:
            print("\nNo students found.")
        else:
            print("\n--- Student Records ---")

            for student in students:
                # Print the student records
                print(
                    f"ID: {student[0]} | "
                    f"Name: {student[1]} {student[2]} | "
                    f"Email: {student[3]} | "
                    f"Enrollment Date: {student[4]}"
                )

    except psycopg2.Error as error:
        print("Error retrieving students:", error)

    finally:
        cursor.close()
        connection.close()


# 2. Add a new student
def addStudent(first_name, last_name, email, enrollment_date):
    connection = connectToDatabase()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        # Insert a new student record into the database
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) " \
            "VALUES (%s, %s, %s, %s);", 
            (first_name, last_name, email, enrollment_date))

        connection.commit()
        print(f"\nStudent {first_name} {last_name} added successfully.")

    # Handle any errors that occur during the insertion
    except psycopg2.Error as error:
        connection.rollback()
        print("Error adding student:", error)

    finally:
        cursor.close()
        connection.close()


# 3. Update a student's email address
def updateStudentEmail(student_id, new_email):
    connection = connectToDatabase()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        # Update the email address of a specific student in the database
        cursor.execute("UPDATE students " \
            "SET email = %s " \
            "WHERE student_id = %s;", 
            (new_email, student_id))

        connection.commit()

        # Check if any rows were affected by the email update
        if cursor.rowcount > 0:
            print(f"\nEmail for student {student_id} updated successfully.")
        else:
            print(f"\nNo student found with ID {student_id}.")

    # Handle any errors that occur during the email update
    except psycopg2.Error as error:
        connection.rollback()
        print("Error updating student email:", error)

    finally:
        cursor.close()
        connection.close()


# 4. Delete a student
def deleteStudent(student_id):
    connection = connectToDatabase()

    if connection is None:
        return

    try:
        cursor = connection.cursor()

        # Delete a specific student record from the database
        cursor.execute("DELETE FROM students " \
            "WHERE student_id = %s;", 
            (student_id,))

        connection.commit()

        # Check if any rows were affected by the deletion
        if cursor.rowcount > 0:
            print(f"\nStudent {student_id} deleted successfully.")
        else:
            print(f"\nNo student found with ID {student_id}.")

    # Handle any errors that occur during the deletion
    except psycopg2.Error as error:
        connection.rollback()
        print("Error deleting student:", error)

    finally:
        cursor.close()
        connection.close()


# Main application menu
def main():
    while True:
        # Print main menu options
        print("\n--- Student Management System ---")
        print("1. Display all students")
        print("2. Add a student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("5. Exit")

        # Get and handle menu user inputs
        choice = input("\nEnter your choice (1-5): ")

        # Display all students
        if choice == "1":
            getAllStudents()

        # Add a new student
        elif choice == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")

            # Make sure that the date is in the correct format
            try:
                datetime.strptime(enrollment_date, "%Y-%m-%d")
                addStudent(first_name, last_name, email, enrollment_date)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD and use a valid date.")

        # Update a student's email
        elif choice == "3":
            # Make sure that the student ID is an integer
            try:
                student_id = int(input("Enter student ID: "))
                new_email = input("Enter new email address: ")
                updateStudentEmail(student_id, new_email)
            except ValueError:
                print("Student ID must be an integer.")

        # Delete a student
        elif choice == "4":
            # Make sure that the student ID is an integer
            try:
                student_id = int(input("Enter student ID: "))
                deleteStudent(student_id)
            except ValueError:
                print("Student ID must be an integer.")

        # Exit the application
        elif choice == "5":
            print("\nExiting Student Management System.")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
