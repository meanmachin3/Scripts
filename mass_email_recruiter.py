# 1. Make sure to change resume/pdf location before sending email.
# 2. Change the content of email
# 3. Add all recruiter email in recruiter_email.txt on each line
# TODO: Code clean up, use env variable, add database to send email?

import yagmail
GMAIL_USERNAME = ''
GAMIL_PASS = ''
yag = yagmail.SMTP(GMAIL_USERNAME, GAMIL_PASS)

contents = ["Sir/Ma'am", "\n", "Hope you are doing well", "\n" , "I am currently pursuing a Master’s of Science in Computer Science at University of Florida. Completed my graduation with a double degree (B.Tech and M.Tech) in Metallurgical Engineering and Material Science at Indian Institute of Technology Bombay. Have worked at SumTotal Systems (a Skillsoft company) as Software Engineer on a variety of payroll and HR products in an agile development environment.", "\n", 
"I worked as a software developer where the nature of the work includes designing and implementing applications for tax and payroll requirements, responding to high priority customer escalations and producing bespoke changes in line with individual customer requirements and in the process I have learned the theoretical and practical aspects of product life cycle and implementation of various programming languages at different stages.  I worked on both front and back-ends, basically a full stack developer for the product, utilizing Java 8 (JEE), Spring Framework (Security, MVC, Transaction Management), Web Services (RESTful), XML (DOM, SAX, JAXB) JavaScript (ExtJS), JSPs, JUnit, Mockito, Hibernate, JDBC, SQL Server.", "\n", "Please find the attached resume with this mail.", "\n", "/Users/meanmachin3/Desktop/NikunjSarda.pdf", "Regards, ", "Nikunj Sarda", "Master Student in CS", "Univeristy of Florida"]


filepath = 'recruiter_email.txt'

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Sending mail  {}: {}".format(cnt, line.strip()))
       yag.send(line.strip(), 'Potential Candidate: Software Engineering (New Graduate)', contents)
       line = fp.readline()
       cnt += 1

