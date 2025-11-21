Restaurant Dining Reservation System

A simple Python-based console application for managing restaurant reservations.

📌 Overview

This project is a console-based Restaurant Dining Reservation System developed in Python.
It allows users to:

View existing reservations

Create new reservations

Delete existing reservations

Generate summarized reports

Save and load reservations using a text file

The system uses Object-Oriented Programming (OOP), file handling, and exception handling.

🗂️ Features
✅ 1. View Reservations

Displays a list of all saved reservations from reservations.txt.

✅ 2. Make a Reservation

Prompts the user to enter:

Name

Date

Time

Number of adults

Number of children

Automatically calculates subtotal using:

Adult rate: PHP 500

Child rate: PHP 300

✅ 3. Delete Reservation

Removes a reservation by selecting its number in the list.

✅ 4. Generate Report

Shows:

Each reservation with subtotal

Total adults

Total children

Grand total revenue

✅ 5. Auto Save/Load

Reservations are stored in the file:

reservations.txt


The system loads and saves automatically.

💻 How to Run

Make sure Python is installed.

Save the script (e.g., reservation_system.py).

Run the program:

python reservation_system.py


The system will generate or use the file:

reservations.txt

📁 File Structure
reservation_system.py
reservations.txt   ← auto-created when saving data

🧱 Class Structure
Reservation Class

Handles:

Guest info

Subtotal calculation

Converting data to/from file format

ReservationSystem Class

Handles:

Loading/saving file

Viewing reservations

Adding reservations

Deleting reservations

Generating reports

🧾 Sample Reservation Entry in File
Nov 10, 2024|10:00 am|John Doe|2|1


Format:

date | time | name | adults | children

👤 Author

James N. Jamero
BSIT Student – Restaurant Dining Reservation System Project
