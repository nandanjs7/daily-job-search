import smtplib, os
from email.mime.text import MIMEText

msg = MIMEText(open("jobs.txt", encoding="utf-8").read())
msg["Subject"] = "Daily Job Listings"
msg["From"] = os.getenv("EMAIL_USER")
msg["To"] = os.getenv("EMAIL_TO")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
    s.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
    s.send_message(msg)
