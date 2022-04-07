import imaplib
M = imaplib.IMAP4_SSL('imap.gmail.com')

#credentials
email = ("YOUR_EMAIL")
password = ("YOUR_APP_PASSWORD")
M.login(email,password)
M.list()

#fetching email
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
        # print("\033[1mSubject: \033[0m\n" + subject)
        print(f"\033[1;30;47mRE: {subject}\033[0m")
        for i in range(2):
            print(" ")
            
        #formatter
        formatted_body = str(body).replace("\\r\\n","\r\n").replace("'", "").replace("\\n", "\n").replace("\\", "").replace("  ","\n")
        body2 = formatted_body[1:]
        print(f"\033[1m{body2}\033[0m")

