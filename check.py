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

# Get the current date and time
current_time = datetime.datetime.now()

# Convert the current time to a formatted string
formatted_time = current_time.strftime("[%Y-%m-%d %H:%M:%S]")
  
pytonProcess = subprocess.check_output("ps aux | grep spigot",shell=True).decode() 
pytonProcess = pytonProcess.split('\n') 
currently_Running = False  
for process in pytonProcess: 
    print(process)
    if 'spigot' in process and "grep" not in process:
        currently_Running = True
        good_process = process
if currently_Running == True:
        print("["+formatted_time+"] Lookin good. It's running: {good_process}")
else:
    print("Well, it's not running... maybe try restarting?")    
    restartshell = subprocess.Popen("su root", Shell=True)
    restartshell.stdin.write("kali").encode()
    restartshell.stdin.write("cd").encode()
    restartshell.stdin.write("screen -r main")
    tryRunning = subprocess.check_output("readlink -f start.sh", shell=True).decode()
    restartshell.stdin.write(tryRunning)
