import smtplib
import ssl
from email.message import EmailMessage

def send_email():
    print("\n--- Email Automation Tool ---")
    
    sender_email = input("Sender Email: ").strip()
    sender_password = input("Sender App Password: ").strip()
    receiver_email = input("Receiver Email: ").strip()
    subject = input("Subject: ").strip()
    body = input("Message Body: ")

    # Construct the email
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # SMTP Settings for Gmail
    smtp_server = "smtp.gmail.com"
    port = 465 
    context = ssl.create_default_context()

    try:
        print("Connecting to server...")
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("Success: Email sent successfully!")
            
    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Check your email or App Password.")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    send_email()