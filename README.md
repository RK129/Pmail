# Emailing
Sending and receiving emails using python. 
<br>Finest UI optimization python and tkinter can offer(not much😔)



**Sending(runs from terminal)**<br>
* Sends email with subject and body.<br>
* Will send abbreviations that can be custom made using `.replace()` in the formatter. <br>
* > Example: "OMW" is sent as "on my way"

**Sending(runs from terminal but opens graphical interface)**

* graphical interface to send emails. Graphical version of **sending**<br>
* can save email from menu
* Does not support the formatter or encoder and can't send line breaks, however can send new lines<br>

**Receiving(runs from terminal)**
<br>
* Lists 10 newest emails you have recieved with the email's sender, receiver, and subject. Number of emails displayed can be changed<br>
* Asks you which email you want to open using the email's subject(email you can open is not limited to the listed emails, list is just a suggestion).<br>
* Once opened, it will display the email using utf-8 encoder and custom formatter.

**Formatter**

* Replaces double spaces with a new line. 
* Renders abbreviations using  `.replace()`. 


**Coming soon**

* Being abe to send line breaks and new lines that can be rendered and displayed on all email platforms(gmail, outlook, etc.). Currently only option is to put two spaces and will only be rendered on this program using the formatter


