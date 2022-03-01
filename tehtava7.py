import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()
server.ehlo()

server.login("olli.testi.omena@gmail.com", "Salasana")

msg = "\nHello!" # The /n separates the message from the headers (which we ignore for this example)
server.sendmail("olli.testi.omena@gmail.com", "olli.uronen@gmail.com", msg)