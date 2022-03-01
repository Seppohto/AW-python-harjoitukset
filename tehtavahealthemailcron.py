import requests
import smtplib
from datetime import datetime


url = "http://13.95.70.19/health.html"
r = requests.get(url)
if r.status_code == 200 :
    print(r)

try:
    with open('testiv5.txt', 'a') as i :
        i.write('\nAccessed on ' + str(datetime.now()))
    
except:
    print("An exception occurred")
else :
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("olli.testi.omena@gmail.com", "Salasana")

    msg = "\nHello!" # The /n separates the message from the headers (which we ignore for this example)
    server.sendmail("olli.testi.omena@gmail.com", "olli.uronen@gmail.com", msg)