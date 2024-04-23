import subprocess 
import datetime
  
pytonProcess = subprocess.check_output("ps aux | grep spigot",shell=True).decode() 
pytonProcess = pytonProcess.split('\n') 
currently_Running = False  
for process in pytonProcess: 
    print(process)
    if 'spigot' in process:
        currently_Running = True
        good_process = process
if currently_Running == True:
        print("["+datetime.datetime()+f"] Lookin good. It's running: {good_process}")
else:
    print("Well, it's not running... maybe try restarting?")    
    restartshell = subprocess.Popen("su root", Shell=True)
    restartshell.stdin.write("kali \n")
    tryRunning = subprocess.check_output("readlink -f start.sh", shell=True).decode()
    restartshell.stdin.write(tryRunning)
