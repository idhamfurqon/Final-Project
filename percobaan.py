import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

f = open('rec_list.txt', 'r').readlines()
for n in f :
    emails = n.rstrip()
    print(emails)


dari = "idhamfurqon@gmail.com"
password = input("Masukkan Password : ")
kepada = emails
msg = MIMEMultipart()

msg['From'] = dari
msg['To'] = kepada
msg['Subject'] = "Judul Pesan1433"

body = "Isi pesan"
html = """/
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
server.sendmail(dari, emails, text)
print("Kirim emil berhasil!")
server.quit()
