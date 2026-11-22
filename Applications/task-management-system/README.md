# Command-Line Task Management System

## What this project is about

**Problem:** Small teams need a reliable way to keep a record of assigned work, deadlines and completed tasks without relying on scattered notes.

I built a text-based task management application in Python. A user can create an account, log in and work with task records, while the administrator can assign work and review reports. The programme runs in a terminal and saves its records to local text files. 

## What I implemented

- User registration and login with separate administrator actions.
- Assigning tasks, including descriptions, dates and responsible users.
- Viewing all tasks or tasks assigned to a particular user.
- Updating, completing and deleting task records.
- Generating task summaries, reports and basic statistics.
- File-based persistence and input validation for command-line use.

## Technology and methods

Python 3, file input/output, functions, conditional logic, loops, input validation and basic reporting.

## How to run

1. Open a terminal in this folder and run `python task_manager.py`.
2. Set a unique `TASK_MANAGER_ADMIN_PASSWORD` environment variable before using administrator functions.
3. Use fictional user data only. Local task and account files are excluded from version control.

## What this demonstrates

Translating a workflow into an interactive application, handling user input, organising code into functions and maintaining records between sessions.

## Security note

The published code reads the administrator password from an environment variable. Regular user passwords are currently stored as plaintext. Use test credentials only; password hashing and stronger access controls would be needed for real accounts.


