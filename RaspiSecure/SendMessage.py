import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sys import argv

def sendMessage(fileName, target = 'vincent@ualberta.ca'):
	# important junk
	username = 'benjc.vincent@gmail.com'
	password = 'Dig1talB3ar'

	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Alert"
	msg['From'] = username
	msg['To'] = target

	# Create the body of the message (a plain-text and an HTML version).
	text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
	htmlfile = open(fileName, 'r')
	html = htmlfile.read()
	htmlfile.close()

	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)

	# start the email server
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)

	server.sendmail(username, target, msg.as_string())

if __name__ == '__main__':
	if len(argv) > 2:
		send(argv[1], argv[2])
	else :
		send(argv[1])