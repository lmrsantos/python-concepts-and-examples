# How to grab emails using imaplib
import imaplib
import getpass
import email ## built-in method to manipulate the email in string format
import chardet

# 1 - Instantiate the object
imap = imaplib.IMAP4_SSL("imap.gmail.com")

# 2 - get email and password
username = getpass.getpass("Username: ")
psw = getpass.getpass("Password: ")  # this isn't your email password. This is the APP_KEY that you can get on your email provider website 

# 3 - Login
imap.login(username, psw)

# 4 - Select the folder you want to check
# print (imap.list())
imap.select("inbox")

# 5 - Define what you are looking for - SEARCH options below
'''
ALL: Matches all messages.
ANSWERED: Matches messages that have the \Answered flag set.
BCC: Matches messages where the specified address is in the BCC field.
BEFORE: Matches messages that have a date before the specified date.
BODY: Matches messages where the specified text is found in the body of the message.
CC: Matches messages where the specified address is in the CC field.
DELETED: Matches messages that have the \Deleted flag set.
DRAFT: Matches messages that have the \Draft flag set.
FLAGGED: Matches messages that have the \Flagged flag set.
FROM: Matches messages where the specified address is in the From field.
GREATER: Matches messages that have a date greater than the specified date.
HEADER: Matches messages where the specified header field contains the specified text.
KEYWORD: Matches messages that have the specified keyword flag set.
NEW: Matches messages that do not have the \Seen flag set.
ON: Matches messages that have the specified date.
OR: Performs a logical OR operation on two or more search criteria.
SENTBEFORE: Matches messages that have a date before the specified date and the \Sent flag set.
SENTON: Matches messages that have the specified date and the \Sent flag set.
SENTSINCE: Matches messages that have a date after the specified date and the \Sent flag set.
SINCE: Matches messages that have a date after the specified date.
SUBJECT: Matches messages where the specified text is found in the subject line of the message.
TEXT: Matches messages where the specified text is found in the body of the message or in any of the headers.
TO: Matches messages where the specified address is in the To field.
UID: Matches messages with the specified UID.
'''
# typ, data = imap.search(None,"FROM '<ADD YOUR STRING HERE>'") ## grab only the IDs
typ, data = imap.search(None,"ON 05-Oct-2023") ## grab only the IDs

email_id = data[0]

list_emails = data[0].split()
ans  ="Y"
# 6 - Manipulate the data that you grab using email build-in method or by scriping one by yourself
for item in list_emails:
    ## Option #1: using message_from_string
    # result, email_data = imap.fetch(item, '(RFC822)')   ## grab the data for each ID
    # encod = chardet.detect(email_data[0][1])['encoding']
    # raw_email_string = email_data[0][1].decode(encod)  ## need to tell Python it is utf-8 to transform the data into a string data
    # email_message = email.message_from_string(''.join(raw_email_string))

    ## Option #2: using message_from_bytes
    email_data = imap.fetch(item, '(RFC822)')[1][0][1]   ## grab the data for each ID
    email_message = email.message_from_bytes(email_data)
    print (f'\n')
    print (email_message['from'])
    print (email_message['date'])
    print (email_message['SUBJECT'])
    for line in email_message.walk():
        if line.get_content_type() == "text/plain":  ## html in case you want to grab some url. Otherwise you can use text/plain
            body = str(line.get_payload(decode=True)).replace('\\r', '\r').replace('\\n', '\n')[2:]
            print (f'{body[0:100]}\n')
            print ("--------------------------")
            ans = input ("Continue? (Y/N)")
            if ans.upper() == "N":
                break
    if ans.upper() == "N":
        break

# 7 - Close session
imap.close