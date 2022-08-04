import smtplib
from email.mime.text import MIMEText as text
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
# smtpserver.ehlo()
smtpserver.starttls()
# smtpserver.ehlo()


emailfetch = open("emailid.txt", 'r')
getidpass = (emailfetch.readline()).split('#')
smtpserver.login(getidpass[0], getidpass[1])

listofuser = ['sunilkumar', 'suni', 'jnanesh']
listofmailid = ['sunilkumarsh38@gmail.com', 'jnaneshvenki@gmail.com']

for i in range(0, len(listofmailid)):
    mailsubmsg = text(
        f"Hi {listofuser[i]},\nyou are promoted ,\nThanks and Regards ,\nSmartenovations")
    mailsubmsg['Subject'] = "Message from sunil for testing "
    smtpserver.sendmail(getidpass[0], listofmailid[i], mailsubmsg.as_string())
smtpserver.quit()
print('done')
