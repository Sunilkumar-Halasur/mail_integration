from email.mime.text import MIMEText as text
import smtplib
from django.db.models.signals import post_save
from django.dispatch import receiver
from. models import Jobdesc


@receiver(post_save, sender=Jobdesc)
def created_success(sender, instance, created, **kwargs):
    if created:

        smtpserver = smtplib.SMTP('smtp.gmail.com', 587)

        smtpserver.starttls()

        emailfetch = open("emailid.txt", 'r')
        getidpass = (emailfetch.readline()).split('#')
        smtpserver.login(getidpass[0], getidpass[1])

        listofuser = ['sunilkumar', 'sunil']
        listofmailid = ['sunilkumarsh38@gmail.com',
                        'sunish096@gmail.com']

        for i in range(0, len(listofmailid)):
            mailsubmsg = text(
                f"Hi {listofuser[i]},\n\nNew job has been posted by Smart Enovations\nPlease click on below link for job description.\n\nhttp://122.166.191.134:8001/login,\nhttp://192.168.1.33:8430/\n\n\nThanks and Regards \nSmart Enovations")
            mailsubmsg['Subject'] = (f"We are hiring..! {instance.title}")
            smtpserver.sendmail(
                getidpass[0], listofmailid[i], mailsubmsg.as_string())
        smtpserver.quit()
        print('done')
