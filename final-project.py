#sumber : https://stackoverflow.com/questions/3362600/how-to-send-email-attachments
import smtplib
from email.mime.multipart import MIMEMultipart        
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

mail = []
#sumber : https://qastack.id/programming/8856117/how-to-send-email-to-multiple-recipients-using-python-smtplib
f = open('rec_list.txt', 'r').readlines()
for n in f :
    emails = n.rstrip(', ')
    mail.append(emails)

dari = "idhamfurqon@gmail.com"
password = input("Masukkan password: ")
#sumber : https://stackoverflow.com/questions/44605843/print-list-elements-in-email-body-list-object-has-no-attribute-encode
kepada = "".join(mail)
msg = MIMEMultipart()

msg['From'] = dari
msg['To'] = kepada
msg['Subject'] = "Judul Pesan"

body = "Isi pesan"
html = """
<!DOCTYPE html>
<html>
    <head>
        <body>
            <div style="border: 0px solid rgb(204, 204, 204); padding: 40px; display: block; background-color: #2E99A5;"> 
                <div style="border: 1px solid rgb(204, 204, 204); padding: 40px; display: block; background-color: #8BD9CA;">
                  <p style="font-size: 20px;"><center>Assalamulaikum [nama]</center></p>
                <p style="font-size: 14px;"> 
                  <br><center>"Selamat Hari Raya Idul Fitri"</br>
                <br>Mohon maaf lahir dan batin</br>
                <br></br>
                <br>Terima  kasih atas bantuan dan dukungan selama ini.</br>
                <br>Semoga relasi kita terus terawat dan terjaga dengan baik serta dapat terus berkerja sama di berbagai kesempatan</center></br>
                
                </p>
                </div>
                </div>
        </body>
    </head>
</html>
"""
#sumber : https://stackoverflow.com/questions/3362600/how-to-send-email-attachments
msg.attach(MIMEText(body, 'plain'))
msg.attach(MIMEText(html, 'html'))

#Lampiran
filename = "foto1.png"
attachment = open("G:/AI_python/foto1.png", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename = %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(dari, password)
print("Berhasil login")
text = msg.as_string()
for a in range(len(mail)):
    server.sendmail(dari, mail[a], text)
    print("Kirim emil berhasil!")
server.quit()
