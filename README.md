# Automation-Script-Pack
Python scripts to automate repetitive tasks like file renaming, data extraction, and sending emails, strengthening skills in scripting, Regex, and automation.
📌 Overview
This project contains a modular set of Python scripts designed to automate common repetitive tasks. It demonstrates core Python capabilities including File I/O, Regular Expressions (Regex), and Network Communication (SMTP).

Included Tools:
File Renamer: Batch renames files in a directory using a custom pattern.

Data Extractor: Scans text files to extract emails and phone numbers using Regex.

Email Automation: Sends emails programmatically via Gmail SMTP.

⚙️ Environment Setup
1. Prerequisites
Python 3.x installed.

No external libraries are required (uses standard libraries: os, re, smtplib, ssl).

2. Email / SMTP Configuration (Crucial)
To use the Email Automation tool with Gmail, you cannot use your standard login password. You must generate an App Password.

Go to your Google Account Settings.

Navigate to Security > 2-Step Verification (Turn it ON if it is off).

Scroll to the bottom of the 2-Step Verification page and look for App passwords.

Create a new app password:

App name: "Python Automation"

Click Create.

Copy the 16-character code generated (e.g., abcd efgh ijkl mnop).

Use this code as your password when running the script.

🚀 How to Run the Project
The project is designed with a central entry point.

Open your terminal or command prompt.

Navigate to the project directory:

Bash

cd path/to/automation_pack
Run the main menu script:

Bash
python main.py
Select a tool by typing the corresponding number (1-4).

<img width="888" height="621" alt="Screenshot 2025-12-16 125955" src="https://github.com/user-attachments/assets/838f546b-de95-4320-90c8-fdcdda6c812b" />
<img width="888" height="118" alt="Screenshot 2025-12-16 130006" src="https://github.com/user-attachments/assets/90ba8fb6-6c12-49eb-9b3c-8fb680b5a2b9" />
<img width="1023" height="355" alt="Screenshot 2025-12-16 130050" src="https://github.com/user-attachments/assets/d2fbfb4f-7bef-4aaa-afc9-faf20dd6570b" />
<img width="1011" height="457" alt="Screenshot 2025-12-16 130315" src="https://github.com/user-attachments/assets/88fd0f26-1f11-44de-9168-f1eac3ff1c14" />





