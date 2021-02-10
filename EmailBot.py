import getpass
import smtplib
import pandas as pd
import time

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

    recipientName = str(row["fname"]) +" "+ str(row["lname"])
    if recipientName == "nan nan" or recipientName == "nan":
        recipientName = ""

    companyName = str(row["company"])
    recipientAddress = str(row["email"])

    subject = "California State University, Sacramento - Computer Science Senior Project Proposal/Volunteer Request"

    text = '''Greetings ''' +  recipientName + ''', 

My name is Joshua Poe. I'm currently a senior in the Computer Science department at California State University, Sacramento. I represent a group of seniors currently seeking the opportunity to volunteer our time, knowledge, and experience over the course of the next two semesters by creating a software application, completely gratis.

Our team consists of eight Computer Science seniors with industry experience and interests ranging from data analytics/data science to cybersecurity, embedded systems, cloud-agnostic solutions, web development, and more. Our team can fill a need ''' + companyName + ''' has been looking for.

We would love the opportunity to bring your passion project to life. We are available this semester to begin creating a high-fidelity prototype with the final product being delivered by December of 2021.

We would be more than excited to meet with you or your team to discuss in more detail the opportunities of volunteering our time and unique abilities.

Please respond to this email at your earliest convenience.

Best Regards,
Joshua Poe

Cell - 916-261-5200
Email - jpoe@csus.edu
Linked In - https://www.linkedin.com/in/joshua-poe/
GitHub - https://github.com/icarus44-zer0
    '''
    try:
        sendMail(server,"jpoe@csus.edu",recipientAddress,subject,text)
        print(recipientName + ", "+ companyName + ", "+ recipientAddress)
        time.sleep(20)
    except:
        print("FAILED " + recipientName + ", "+ companyName + ", "+ recipientAddress)
        pass
    # time.sleep(20)
    return

def main():
    names = ["fname","lname","email", "company"]
    df = pd.read_csv('Email_List.txt', delimiter=",", names=names)
    df.apply(setBody,axis=1)
    return

if __name__ == "__main__":
    main()
