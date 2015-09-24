import urllib2
import json
from datetime import datetime
from email.mime.text import MIMEText
import smtplib
import time


def confirm(title):
    print "In Stock!!"
    me = "me@gmail.com"
    you = "you@gmail.com"
    msg = MIMEText("In Stock!!")
    msg['Subject'] = title
    msg['From'] = me
    msg['To'] = you
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login("username", "password")
    s.sendmail(me, [you], msg.as_string())
    s.quit()
    print "Success!!"


if __name__ == "__main__":
    while 1:
        try:
            plain = urllib2.urlopen("https://reserve.cdn-apple.com/HK/en_HK/reserve/iPhone/availability.json").read()
            data = json.loads(plain)
            print "Last update:", datetime.fromtimestamp(float(data['updated']) / 1000)
            for e in data['R485']:
                if data['R485'][e]:
                    if 'MGA' in e: confirm('iPhone 6s Availability')
                    if 'MG4J2ZP/A' in e: confirm('iPhone 6 Gold 64GB Availability')
            for e in data['R409']:
                if data['R485'][e]:
                    if 'MGA' in e: confirm('iPhone 6s Availability')
                    if 'MG4J2ZP/A' in e: confirm('iPhone 6 Gold 64GB Availability')
            for e in data['R428']:
                if data['R485'][e]:
                    if 'MGA' in e: confirm('iPhone 6s Availability')
                    if 'MG4J2ZP/A' in e: confirm('iPhone 6 Gold 64GB Availability')
        except:
            print "Update failed:", datetime.now()
        time.sleep(30)
