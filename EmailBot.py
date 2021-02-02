import getpass
import smtplib
server = smtplib.SMTP('smtp.csus.edu', 587)
server.starttls()
#enter email username
USER = "Manhsy@csus.edu"

#enter email password
PASSWORD = getpass.getpass(prompt='Password: ', stream=None) 

server.login(USER, PASSWORD)

#compose the subject/body of the email
subject = 'Subject: '
text = 'Message: '
message = "Subject: {}\n\n{}".format(subject, text)

#replace file.txt with the file name that has a list of email addesses
f = open("file.txt", "r")

for x in f:
    recipient = x
    server.sendmail(USER, recipient, message)
f.close()
server.close()

