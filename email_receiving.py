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
ALL                 All messages in the mailbox; the default initial key for ANDing.
ANSWERED            Messages with the \Answered flag set.
BCC <string>        Messages that contain the specified string in the envelope structure's BCC field.
BEFORE <date>       Messages whose internal date is earlier than the specified date.
BODY <string>       Messages that contain the specified string in the body of the message.
CC <string>         Messages that contain the specified string in the envelope structure's CC field.
DELETED             Messages with the \Deleted flag set.
DRAFT               Messages with the \Draft flag set.
FLAGGED              Messages with the \Flagged flag set.
FROM <string>       Messages that contain the specified string in the  envelope structure's FROM field.
HEADER <field-name> <string> Messages that have a header with the specified field-name (as defined in [RFC-822]) and that
                     contains the specified string in the [RFC-822] field-body.
KEYWORD <flag>      Messages with the specified keyword set.
LARGER <n>          Messages with an [RFC-822] size larger than the specified number of octets.
NEW                 Messages that have the \Recent flag set but not the \Seen flag.  This is functionally equivalent to "(RECENT UNSEEN)".
NOT <search-k       Messages that do not match the specified search key.
OLD                 Messages that do not have the \Recent flag set. This is functionally equivalent to "NOT RECENT" (as opposed to "NOT NEW").
ON <date>           Messages whose internal date is within the specified date.
OR <search-key1> <search-key2> Messages that match either search key.
RECENT              Messages that have the \Recent flag set.
SEEN                Messages that have the \Seen flag set.
SENTBEFORE <date>   Messages whose [RFC-822] Date: header is earlier than the specified date.
SENTON <date>       Messages whose [RFC-822] Date: header is within the specified date.
SENTSINCE <date>    Messages whose [RFC-822] Date: header is within or later than the specified date.
SINCE <date>        Messages whose internal date is within or later than the specified date.
SMALLER <n>         Messages with an [RFC-822] size smaller than the specified number of octets.
SUBJECT <string>    Messages that contain the specified string in the envelope structure's SUBJECT field.
TEXT <string>       Messages that contain the specified string in the header or body of the message.
TO <string>         Messages that contain the specified string in the envelope structure's TO field.
UID <message set>   Messages with unique identifiers corresponding to the specified unique identifier set.
UNANSWERED          Messages that do not have the \Answered flag set.
UNDELETED           Messages that do not have the \Deleted flag set.
UNDRAFT             Messages that do not have the \Draft flag set.
UNFLAGGED           Messages that do not have the \Flagged flag set.
UNKEYWORD <flag>    Messages that do not have the specified keyword set.
UNSEEN              Messages that do not have the \Seen flag set.
'''
# typ, data = imap.search(None,"FROM '<ADD YOUR STRING HERE>'") ## grab only the IDs
typ, data = imap.search(None,"FROM 'IMDb' SINCE 21-Sep-2023") ## For clause "AND" leave space between each condition. For "OR" clause use the connector "OR".

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
            r = input("Mask as (R)ead or (D)elete it: ").upper()
            if r == "D":
                imap.store(item, "+FLAGS", "\\Deleted")
            elif r == "R":
                imap.store(item,"+FLAGS", "\\Seen")
            ans = input ("Continue? (Y/N)")
            if ans.upper() == "N":
                break
    if ans.upper() == "N":
        break

# 7 - Close session
imap.close