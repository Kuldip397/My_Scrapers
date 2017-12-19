from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
import os


def get_file_path(filename):
    file_path = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(file_path):
        raise Exception("This is not a file")
    return file_path


def get_emails(filename):
    file_path = get_file_path(filename)
    return open(file_path).read()


host = "smtp.gmail.com"
port = 587
username = "kkvkicktheworldup7@gmail.com"
password = "%%%%%"

to_list = []
file_contents = get_emails("send_email_to.txt")
to_list = file_contents.split("\n")

try:
    email_conn = SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)

    the_msg = MIMEMultipart("alternative")
    the_msg["Subject"] = "The Mail"
    the_msg["From"] = username

    plain_text = "Hi"
    html_text = """
    <html>
        <head>
            <body>
                <p>
                    hi</br> just sending this mail <h1>bro</h1>
                </p>
            </body>
        </head>
    </html>
    """
    part_1 = MIMEText(plain_text, "plain")
    part_2 = MIMEText(html_text, "html")

    the_msg.attach(part_1)
    the_msg.attach(part_2)

    email_conn.sendmail(username, to_list, the_msg.as_string())
    email_conn.quit()
except:
    print("Cannot login in")
