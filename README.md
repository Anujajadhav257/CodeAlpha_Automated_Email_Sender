# CodeAlpha_Automated_Email_Sender
# Daily Python Learning Topics Email Scheduler

This script sends a daily email at a scheduled time with a list of Python learning topics. The email is sent using Gmail's SMTP server. The sender's email credentials are required for sending the email.

## Features

- **Password Input**: The script securely prompts for the sender's email password using masked input.
- **Scheduled Email**: Automatically sends an email at a specified time every day.
- **Email Content**: The email contains a list of important Python topics to learn.

## Requirements

- Python 3.x
- `smtplib` module (standard library)
- `threading` module (standard library)
- `datetime` module (standard library)
- `time` module (standard library)
- `pwinput` module for masked password input

## Installation

1. **Clone the repository** (or download the script directly):
    ```bash
    git clone https://github.com/yourusername/daily-python-email-scheduler.git
    cd daily-python-email-scheduler
    ```

2. **Install the `pwinput` module**:
    ```bash
    pip install pwinput
    ```

## Usage

1. **Open the script** in a text editor and set the `Sender_Email` and `Rec_Email` variables to the appropriate email addresses.

    ```python
    Sender_Email = "your_sender_email@gmail.com"
    Rec_Email = "recipient_email@gmail.com"
    ```

2. **Run the script**:
    ```bash
    python daily_python_email_scheduler.py
    ```

3. **Enter the password** for the sender's email when prompted. The input will be masked for security.

4. The script will schedule the email to be sent daily at 15:40 PM (3:40 PM). It will print a message indicating the scheduled time.

## Notes

- The scheduled time is set to 15:40 PM (3:40 PM) by default. You can change this time by modifying the `send_time` variable in the `schedule_email` function.
  
    ```python
    send_time = now.replace(hour=15, minute=40, second=0, microsecond=0)
    ```

- Ensure that [less secure app access](https://myaccount.google.com/lesssecureapps) is enabled for the sender's Gmail account to allow the script to send emails. Google may block sign-ins from this script if it deems them as less secure.

## Security

- The sender's email password is taken as input and not stored in the script. It is used only for logging in to the SMTP server and sending the email.

## Troubleshooting

- **Login Issues**: If you encounter login issues, make sure you have enabled less secure app access for the sender's Gmail account.
- **Email Not Sent**: If the email is not sent, ensure that the provided credentials are correct and that there is an active internet connection.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to the project by submitting issues or pull requests. Happy coding!
