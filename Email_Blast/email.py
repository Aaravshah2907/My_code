"""
######################################################################
Simple Text Email Python Script
Coded By "The Intrigued Engineer" over a coffee
Thanks For Watching!!!
######################################################################
"""
import smtplib
import ssl

# Setup port number and server name

smtp_port = 587  # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

email_from = "aaravshah0011@gmail.com"
email_to = "aaravshah0011@gmail.com"

pswd = "elksvwkmsaisydex"

# content of message

message = "Dear god, please help!!!"

# Create context
simple_email_context = ssl.create_default_context()

try:
    # Connect to the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, pswd)
    print("Connected to server :-)")

    # Send the actual email
    print()
    print(f"Sending email to - {email_to}")
    TIE_server.sendmail(email_from, email_to, message)
    print(f"Email successfully sent to - {email_to}")
    # Close the Port
    TIE_server.quit()

# If there's an error, print it out
except Exception as e:
    print(e)
