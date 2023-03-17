import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('guneetmalhotra01@gmail.com','mummy_gunnu@123')
server.sendmail('guneetmalhotra01@gmail.com','guneetmalhotra01@gmail.com','Mail Sent from Python Code')
print('Mail Sent')