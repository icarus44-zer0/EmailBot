import getpass
import smtplib
import pandas as pd


#intialize server for sending email messages
def serverSetup():
    server = smtplib.SMTP('smtp.csus.edu', 587)
    server.starttls()
    USER = ""
    PASSWORD = ""
    server.login(USER, PASSWORD)
    return server

#send the message
def sendMail(server,senderAddress, recipientAddress, subject, body):
    message = "Subject: {}\n\n{}".format(subject, body)
    server.sendmail(senderAddress, recipientAddress, message)
    server.close()

#intialize the body of the email
def setBody(row):
    # recipientName = "".join([row["fname"], row["lname"]], delimiter="/s")
    server = serverSetup()
    recipientName = row["fname"] +" "+ row["lname"]
    companyName = row["company"]
    recipientAddress = row["email"]

    subject = "California State University Sacramento - Computer Science Volunteer Request"

    text = '''Greetings ''' + recipientName + ''', \n\n\t My name is Joshua Poe. I'm a current senior in the Computer Science department at California State University, Sacramento. I represent a group of eight seniors currently seeking the opportunity to volunteer our time, knowledge, and experience over the course of the next two semesters. One of the requirements of our department for graduation is an end of year project / Senior Project that is intended to provide computer science majors with experience in the development of a software application. We would love the opportunity to do some software development work for you and your company completely gratis. I'd greatly enjoy the opportunity to meet and discuss in more detail the possibility of volunteering our abilites to ''' + companyName + ''' Im sure you have a project, or two, in the back of your mind that you haven't had the time to prototype yourself; 

Let us develope it for you. 
    
We would be available to begin work on a project immediately with the final product being delevered by december of 2021.
    
Best,
Joshua Poe
'''
    sendMail(server,"jpoe@csus.edu",recipientAddress,subject,text)
    return

names = ["fname","lname","email", "company"]
df = pd.read_csv('recipientList.txt', delimiter=",", names=names)

#iterate to generate the DF 
df.apply(setBody,axis=1)

# iterate over the DF to send the emails