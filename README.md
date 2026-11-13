# Student Management System

## Overview

This project is a Python application that connects to a PostgreSQL database hosted on a remote OpenStack server. 
It uses a command-line interface to manage student records through CRUD (Create, Read, Update, Delete) operations.

The Python application runs locally on the user's computer, while the PostgreSQL database is hosted remotely on an 
OpenStack server. The application communicates with the database over a network connection using the `psycopg2` library.

## Video Demonstration Link

Here is the link to the video demonstration of this application: 

## Technologies Used

- Python 3.10.0 – Application development
- PostgreSQL – Database management
- psycopg2 – Python library for connecting to PostgreSQL
- pgAdmin 4 – Database administration, creation, and verification
- OpenStack – Remote server hosting the PostgreSQL database

## Project Structure

```
comp3005-a3/
│
├── main.py
└── README.md
└── students.sql (Not needed for running, just there for reference to the queries)
```

## Database Information

The application connects to a PostgreSQL database named "students", hosted on an OpenStack server.

The database was created in pgAdmin 4, using queries. The queries used can be seen in students.sql for reference.

The database and its initial data are already set up on the OpenStack server. There is no need to 
create a local PostgreSQL database or run a local PostgreSQL server. The application connects directly 
to the existing remote database.

The database contains a table named `students` with the following schema:

Name:           | Data Type:  | Constrants:

student_id      | SERIAL      | Primary Key, Auto-Increment
first_name      | TEXT        | NOT NULL
last_name       | TEXT        | NOT NULL
email           | TEXT        | NOT NULL, UNIQUE
enrollment_date | DATE        | n/a

The `students` table is initially populated with the following records:

student_id: | first_name: | last_name:  | email:                  | enrollment_date:

1           | John        | Doe         | john.doe@example.com    | 2023-09-01
2           | Jane        | Smith       | jane.smith@example.com  | 2023-09-01
3           | Jim         | Beam        | jim.beam@example.com    | 2023-09-02

## Requirements

Before running the application, ensure that the following requirements are met:

1. Python version 3.10.0 is installed.
2. The `psycopg2` Python library is installed.
3. An internet connection is available.
4. The Carleton University VPN is connected if running the application off campus.
5. The remote PostgreSQL database is accessible on the OpenStack server.

### Important: Network Access

The PostgreSQL database is hosted on a remote OpenStack server and is not a local database.

If you are:
- On campus: The application can connect to the database through the university network, provided the server is accessible.
- Off campus: You must connect to the Carleton University VPN before running the application. Without the VPN, the connection 
  to the OpenStack server may fail.

Make sure the VPN connection is established before starting the application if you are off campus.

## Setup and Running Instructions

Follow these steps in order to set up and run the application.

### Step 1: Clone the GitHub Repository

Open a terminal (Command Prompt, PowerShell, or a terminal in an IDE) and navigate to the directory on your local maching where 
you want to store the project.

Clone the repository using:

```bash
git clone git@github.com:superemma13/comp3005-a3.git
```

Navigate into the project directory:

```bash
cd comp3005-a3
```

The directory should contain the following files:
- main.py
- README.md
- students.sql

### Step 2: Verify the Python Version

This application was developed and tested using Python 3.10.0, though it will likely work the same with any newer versions of python.

Check your installed Python version by running:

```bash
python --version
```

The expected output is "Python 3.10.0" or newer:

If your system has multiple Python versions installed and it doesn't work with newer versions, you may need to switch to version 
3.10.0 using:

```bash
python3.10 --version
```

If Python 3.10.0 is not installed and this application doesn't work with newer versions, install version 3.10.0 before proceeding.

### Step 3: Install the Required Python Library

The application uses `psycopg2` to establish a connection between Python and the PostgreSQL database.

Install the required library on your local machine by running:

```bash
python -m pip install psycopg2-binary
```

Using `python -m pip` ensures that the library is installed for the Python interpreter used to run the application.

To verify that the installation was successful, run:

```bash
python -c "import psycopg2; print('psycopg2 installed successfully')"
```

You should see:

```text
psycopg2 installed successfully
```

### Step 4: Connect to the Carleton University VPN (If Off Campus)

This step is required when running the application from off campus.

Since the PostgreSQL database is hosted on a remote OpenStack server, access to the server requires a connection through the Carleton University network.

1. Open the Carleton University VPN client (Cisco).
2. Connect to the Carleton University VPN using your university credentials.
3. Verify that the VPN connection is active.
4. Keep the VPN connected while running the application.

If you are already connected to the Carleton University campus network, you can proceed without connecting to the VPN.

### Step 5: Run the Application

Once Python and the required library are installed and network access has been established, run the application from the project directory:

```bash
python main.py
```

The following menu will appear:

```
--- Student Management System ---
1. Display all students
2. Add a student
3. Update a student's email
4. Delete a student
5. Exit

Enter your choice (1-5):
```

Enter the corresponding number to perform the desired operation.

At the beginning of each operation, the application will attempt to establish a connection to the remote PostgreSQL database. The operation
will occur if there the connection is successfull.

The application will continue displaying the menu after each operation until option "5" is selected.

## Application Function Descriptions

The application implements the following four CRUD operations:

### 1. Display All Students – getAllStudents()

Retrieves all records from the "students" table using a SQL SELECT statement.

The application displays each student's:
- Student ID
- First name
- Last name
- Email address
- Enrollment date

Records are displayed in ascending order by student ID.

### 2. Add a Student – addStudent(first_name, last_name, email, enrollment_date)

Inserts a new student record into the "students" table using a SQL INSERT statement.

The application prompts the user to enter:
- First name
- Last name
- Email address
- Enrollment date (YYYY-MM-DD)

The enrollment date is validated before the insertion is attempted. If the date is invalid or does not follow the required format, an error 
message is displayed, and you are brought back to the main menu.

The database automatically generates the new student's "student_id". Every student id is unique, even if the student was previously removed.

### 3. Update a Student's Email – updateStudentEmail(student_id, new_email)

Updates the email address of an existing student using a SQL UPDATE statement.

The application prompts the user for:
- The student ID of the record to update
- The new email address

The application checks whether a record with the specified student ID exists and displays a success or error message.

### 4. Delete a Student – deleteStudent(student_id)

Deletes an existing student record using an SQL DELETE statement.

The application prompts the user for the student ID of the record to delete.

The application checks whether a matching student exists and reports whether the deletion was successful.

## Error Handling

The application includes basic error handling to prevent unexpected input or database errors from terminating the program.

- Database connection errors: Connection failures are caught and displayed to the user.
- Invalid enrollment dates: Dates must be valid and follow the YYYY-MM-DD format.
- Invalid student IDs: Student IDs must be integers.
- Non-existent student IDs: The application informs the user if no matching student is found during an update or deletion.
- Database operation errors: Failed INSERT, UPDATE, and DELETE operations trigger a rollback to prevent incomplete transactions.
- Database constraints: PostgreSQL enforces the primary key, NOT NULL, and UNIQUE constraints.
