import getpass
from os import access
import smtplib
import pandas as pd


server = smtplib.SMTP('smtp.csus.edu', 587)
server.starttls()


#intialize server for sending email messages
def serverSetup():

    #enter email username for CSUS.edu
    USER = "jpoe@csus.edu"

    #enter email password
    PASSWORD = getpass.getpass(prompt='Password: ', stream=None) 
    server.login(USER, PASSWORD)

#send the message
def sendMail(senderAddress, recipientAddress, subject, body):
    message = "Subject: {}\n\n{}".format(subject, body)
    server.sendmail(senderAddress, recipientAddress, message)
    server.close()

#intialize the body of the email
def setBody(row):
    recipientName = "".join([row["fname"], row["lname"]], delimiter="/s")
    companyName = row["company"]
    recipientAddress = row["address"]

    subject = 'Sacramento State Computer Science Volunteer Request'
    text = 'Greetings ' + recipientName + ",\n" + '''\tMy name is Joshua Poe. I'm a current senior in the Computer Science department at California State University, Sacramento. I represent a group of eight seniors currently seeking the opportunity to volunteer our time, knowledge, and experience over the course of the next two semesters. One of the requirements of our department for graduation is an end of year project / Senior Project that is intended to provide computer science majors with experience in the development of a software application. We would love the opportunity to do some software development work for you and your company completely gratis.
    I'd greatly enjoy the opportunity to meet and discuss in more detail the possibility of volunteering our abilites to Cal Fire.
    Do you have a project, or two, in the back of your mind that you haven't had the time to prototype yourself? Let us develop it for you. We would be available to begin work on a project immediately with the final project being completed by december of 2021.
    development of a software application for ''' + companyName + ''' Wed love to have the opportunity to do some software development work for you completely gratis. 
    Im sure you have a project, or two, in the back of your mind that you haven't had the time to prototype yourself; 
    let us develope it for you. We would be available to begin work on a project immediately with the 
    final project being completed by december of 2021.'''
    sendMail("jpoe@csus.edu",recipientAddress,subject,text)
    return

serverSetup()

names = ["fname","lname","email", "company"]
df = pd.read_csv("recipientList.txt", delimiter='\s', names=names)

# fname = df["fname"].tolist()
# lname = df["lname"].tolist()
# address = df["email"].tolist()
# company = df["Company"].tolist()

#iterate to generate the DF 
df.apply(setBody,axis=1)

# iterate over the DF to send the emails