from tkinter import*
import smtplib
from tkinter.filedialog import asksaveasfile

smtp_object = smtplib.SMTP("smtp.gmail.com",587)
smtp_object.ehlo()
smtp_object.starttls()
email = ("YOUR_EMAIL")
password = ("YOUR _APP_PASSWORD")
smtp_object.login(email,password)
from_address = email

root = Tk()
root.title('mail')



def save():
	Files = [('All Files', '*.*'),
			('Python Files', '*.py'),
			('Text Document', '*.txt')]
	file = asksaveasfile(filetypes = Files, defaultextension = Files)
def submit():
    to_address = to_addressasked.get()
    subject = subjectasked.get()
    body = bodyasked.get()
    msg = f"Subject: {subject}\n{body}"
    smtp_object.sendmail(from_address,to_address,msg)
    myLabel = Label(root, text="Sent!")
    myLabel.config(font=('Aerial', 35))
    myLabel.pack()





label= Label(root, text= "Who would you like to message?", font= ('Aerial', 40))
label.pack()
to_addressasked = Entry(root)
to_addressasked.pack()
to_addressasked.config(width=30)
to_addressasked.config(font=('Ink Free', 50))

label2= Label(root, text= "Subject:", font= ('Aerial', 40))
label2.pack()
subjectasked = Entry(root)
subjectasked.pack()
subjectasked.config(width=30)
subjectasked.config(font=('Ink Free', 50))

label3= Label(root, text= "Body:", font= ('Aerial', 40))
label3.pack()
bodyasked = Entry(root)
bodyasked.pack()
bodyasked.config(width=30)
bodyasked.config(font=('Ink Free', 50))
label4 = Label(root, text="\n\n\n",font=('Aerial', 30))

submit = Button(root, text="Send",command=submit, width=20, height=2, font=('Aerial', 30))
submit.pack()




menubar = Menu(root)
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='Save', command = lambda : save())
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)
root.config(menu = menubar)

root.mainloop()
