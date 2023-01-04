import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "swarp039@gmail.com"
password = "fjuakrlfpchqtgnh"

receiver = "swarp039@gmail.com"

message = """How are you?"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)