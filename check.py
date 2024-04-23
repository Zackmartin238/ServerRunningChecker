import subprocess 
import datetime

pythonProcess = subprocess.check_output("ps aux | grep spigot", shell=True).decode() 
pythonProcess = pythonProcess.split('\n') 
currently_Running = False  
for process in pythonProcess: 
    print(process)
    if 'spigot' in process:
        currently_Running = True
        good_process = process

if currently_Running:
    print(f"[{datetime.datetime.now()}] Lookin good. It's running: {good_process}")
else:
    print("Well, it's not running... maybe try restarting?")    
    try:
        restartshell = subprocess.Popen(["su", "root"], stdin=subprocess.PIPE, shell=True)
        restartshell.communicate(input="kali\n".encode())
        tryRunning = subprocess.check_output("readlink -f start.sh", shell=True).decode().strip()
        restartshell.communicate(input=tryRunning.encode())
    except Exception as e:
        print(f"An error occurred: {e}")
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
