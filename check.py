import subprocess 
import datetime

pythonProcess = subprocess.check_output("ps aux | grep spigot", shell=True).decode() 
pythonProcess = pythonProcess.split('\n') 
currently_Running = False  
for process in pythonProcess: 
    print(process)
    if 'spigot' in process and "grep" not in process:
        currently_Running = True
        good_process = process

if currently_Running:
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"[{formatted_time}] Lookin good. It's running: {good_process}")
else:
    print("Well, it's not running... maybe try restarting?")    
    try:
        restartshell = subprocess.Popen(["sudo", "su", "root"], stdin=subprocess.PIPE)
        restartshell.communicate(input="kali\n".encode())
        restartshell.communicate(input="cd\n".encode())
        tryRunning = subprocess.check_output("readlink -f start.sh", shell=True).decode().strip()
        subprocess.Popen(tryRunning, shell=True)
    except Exception as e:
        print(f"An error occurred: {e}")
