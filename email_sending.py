# Sending and receiving email 

## 1 - Import the library
import smtplib
import getpass
import os
psw = os.getenv("GMAIL_APP_KEY")
username = "luizmrdsantos@gmail.com"

## 2 - Instantiate the object
smtp_object = smtplib.SMTP("smtp.gmail.com", 587)

## 3 - Stablish the connection, must be done immetiatly after create the object (step #2)
smtp_object.ehlo()
smtp_object.starttls() # because it is using port 587

## 4 - LOGIN - Don't forget to protect your password using getpass lib
# username = getpass.getpass("Enter your email: ")
# psw = getpass.getpass("Password: ")
smtp_object.login(username, psw)

## 5 - Build the message: email_from, email_to, subject and body
email_from = username
email_to = username
subject = input ("Subject: ")
body_msg = input ("Message: ")
msg = "Subject: "+subject+"\n"+body_msg # the message must be connected like this. \n is necessary to separate subject from the body

## 6 - Send the email itself
smtp_object.sendmail(email_from, email_to, msg)

## 7 - Close the connection
smtp_object.quit()
