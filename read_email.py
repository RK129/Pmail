import imaplib                              
import email
from email.header import decode_header
import webbrowser
import os
  
M = imaplib.IMAP4_SSL('imap.gmail.com')
server ="imap.gmail.com"                     
imap = imaplib.IMAP4_SSL(server)
  
username ="YOUR_EMAIL" 
password ="YOUR_APP_PASSWORD"
  imap.login(username, password)               
  
# select the e-mails
res, messages = imap.select('inbox')   
messages = int(messages[0])
 
# determine the number of e-mails to be fetched
n = 10
  
for i in range(messages, messages - n, -1):
    res, msg = imap.fetch(str(i), "(RFC822)")     
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
              
            # getting the sender's mail id
            From = msg["From"]
  
            # getting the subject of the sent mail
            subject = msg["Subject"]

            to = msg['to']
  
            # printing the details
            print("\n")
            print(f"\033[1mFrom: \033[0m{From}")
            print(f"\033[1mTo: \033[0m{to}")
            print(f"\033[1mSubject: \033[0m{subject}")


import imaplib
M = imaplib.IMAP4_SSL('imap.gmail.com')
email = ("Your_EMAIL")
password = ("YOUR_APP_PASSWORD")
M.login(email,password)
M.list()
subject = input("What is the subject of the email? ")
M.select("inbox")
typ, data = M.search(None, f'SUBJECT "{subject}"')
email_id = data[0]
result, email_data = M.fetch(email_id, '(RFC822)')

#email_data
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
import email
email_message = email.message_from_string(raw_email_string)

#encoder
for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(f"\033[1;30;47mRE: {subject}\033[0m")
        for i in range(2):
            print(" ")
            
        #formatter
        formatted_body = str(body).replace("\\r\\n","\r\n").replace("'", "").replace("\\n", "\n").replace("\\", "").replace("  ","\n")
        body2 = formatted_body[1:]
        print(f"\033[1m{body2}\033[0m")



