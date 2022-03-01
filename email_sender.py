from getpass import getpass
import smtplib
import ssl
from email.message import EmailMessage

#konu
subject = "Pythondan Email"
#gövde
body = "Test Maili"

sender_email= "test@gmail.com"
receiver_email = "alici@gmail.com"
password = getpass("Şifrenizi Girin: ")


message = EmailMessage()
message["From"] = sender_email #gönderen
message["To"] = receiver_email #gönderilen
message["Subject"] = subject   #konusad
message.set_content(body)      #mesaj


#gmailin standart bağlantı adresini kullanıyoruz
#smtplib kullanarak gmail serverlarına bağlanıyoruz ssl gerekli bunun için
context = ssl.create_default_context()

print("Gönderiliyor...")

#gmail serverinne bağlanıyoruz
with smtplib.SMTP_SSL("smtp.gmail.com",465, context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message.as_string())

print("Gönderildi.")


#Mailleri okumak için imaplib kullanılıyor
