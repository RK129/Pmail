import smtplib
import getpass


smtp_object = smtplib.SMTP("smtp.gmail.com",587)
smtp_object.ehlo()
smtp_object.starttls()


# email = input("Email:")
# password = getpass.getpass("Password: ")
print("Hello \033[1m YOUR_EMAIL  \033[0m")
for i in range(2):
    print(" ")
email = ("YOUR_EMAIL")
password = ("YOUR_APP_PASSWORD")
smtp_object.login(email,password)

from_address = email
to_address = input("Who would you like to message?\033[1m ")

print("Sending to \033[3;30;47m(" + to_address + ")\033[0m")

for i in range(2):
    print(" ")

subject = input("\033[0mSubject:\033[1m ")
for i in range(2):
    print("\033[0m ")
message = input("Body: \033[1m")
msg = "Subject: "+subject+"\n"+message

smtp_object.sendmail(from_address,to_address,msg)

print("\033[1mSent!")
