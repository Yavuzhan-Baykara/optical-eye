import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


class EmailSender:
    _instance = None

    @staticmethod
    def get_instance():
        if EmailSender._instance is None:
            EmailSender._instance = EmailSender()
        return EmailSender._instance

    def send_email(self, ui12, mail_data, key_data, mail_list, send_pdf_file, body_text):
        try:
            for recipient in mail_list:
                message = MIMEMultipart()
                message["From"] = mail_data
                message["To"] = recipient
                message["Subject"] = "Otomatik Email Gönderme"

                message.attach(MIMEText(body_text, "plain"))

                file_name = os.path.basename(send_pdf_file)
                with open(send_pdf_file, "rb") as f:
                    attach = MIMEApplication(f.read(), _subtype="pdf")
                    attach.add_header("Content-Disposition", "attachment", filename=str(file_name))
                    message.attach(attach)

                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login(mail_data, key_data)
                server.sendmail(mail_data, recipient, message.as_string())
                server.quit()

                print(f"{recipient} adresine e-posta başarıyla gönderildi.")
                ui12.statusbar.showMessage(" "*1 + f"{recipient} adresine e-posta başarıyla gönderildi.", 1500)
        except Exception as e:
            print(f"E-posta gönderme hatası: {e}")
            ui12.statusbar.showMessage(" "*1 + f"E-posta gönderme hatası: {e}", 10000)
            
