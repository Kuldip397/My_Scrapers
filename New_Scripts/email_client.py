import email
import imaplib

username = "kkvkictheworldup7@gmail.com"
password = "kkvrbi#cr77"

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)

mail.select("inbox")