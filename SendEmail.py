import smtplib
import getpass
obj = smtplib.SMTP('smtp.gmail.com',587)
obj.ehlo()  
obj.starttls()
Email = 'harshadchavanirctc@gmail.com'
passsword = ''
obj.login(Email,passsword)
from_email = Email
To_email = 'harshadchavan141@gmail.com'
subject = 'Sending Email from Python Script'
message = 'Subject:' + subject + '\n' + 'testing'
obj.sendmail(from_email,To_email,message)
