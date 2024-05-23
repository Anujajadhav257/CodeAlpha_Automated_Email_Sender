import smtplib
import threading
from datetime import datetime, timedelta
import time
from pwinput import pwinput

def enter_password():
    # Prompt the user to enter their password with masked input
    password = pwinput(prompt="Enter password: ", mask="*")

    # Print the entered password length masked with asterisks
    print(f"Password: {'*' * len(password)}")  # Mask the password when printing

    return password

# Define the sender email and recipient email
Sender_Email = "anuja376079@gmail.com"
Rec_Email = "jadhavanuja2599@gmail.com"

# Get the password from the user
password = enter_password()

def send_email():
    subject = "Daily Python Learning Topics"
    body = (
        "Hey Anuja,\n\n"
        "Here are some important topics for you to learn in Python today:\n\n"
        "1. Python Basics\n"
        "2. Data Structures (Lists, Tuples, Dictionaries, Sets)\n"
        "3. Control Flow (if, for, while loops)\n"
        "4. Functions and Modules\n"
        "5. File Handling\n"
        "6. Exception Handling\n"
        "7. Object-Oriented Programming\n"
        "8. Working with Libraries (NumPy, Pandas, etc.)\n\n"
        "Keep up the good work and happy coding!\n\n"
        "Best regards,\n"
        "Your Python Tutor"
    )
    message = f"Subject: {subject}\n\n{body}"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(Sender_Email, password)
        print("Login successful")
        server.sendmail(Sender_Email, Rec_Email, message)
        print(f"Email has been sent to {Rec_Email}")
    finally:
        server.quit()

# Set up schedule to send email at 12:40 PM daily
def schedule_email():
    now = datetime.now()
    send_time = now.replace(hour=15, minute=40, second=0, microsecond=0)  # Set the time to 15:40 PM

    if now > send_time:
        send_time += timedelta(days=1)  # If it's already past 15:40 PM, schedule for the next day

    delay = (send_time - now).total_seconds()
    timer = threading.Timer(delay, send_email)
    timer.start()

    print(f"Email will be sent at {send_time}")

print("Scheduler started. Waiting for scheduled tasks...")
schedule_email()

# Keep the main thread alive
while True:
    time.sleep(1)
