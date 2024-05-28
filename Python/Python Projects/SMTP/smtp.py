import smtplib
import getpass

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM = "ycce_shreyash-pardhi@outlook.com"
TO = ""
PASS = getpass.getpass("Enter Password: ")

MESSAGE = """Subject: Hi
hi hello,

this is sample mail.

thank you."""

smtp = smtplib.SMTP(HOST, PORT)

statusCode, res = smtp.ehlo()
print(f"[*] Echoing the server: {statusCode}, {res}")

statusCode, res = smtp.starttls()
print(f"[*] Starting TLS connection: {statusCode}, {res}")

statusCode, res = smtp.login(FROM, PASS)
print(f"[*] logging in: {statusCode}, {res}")

smtp.sendmail(FROM, TO, MESSAGE)
smtp.quit()