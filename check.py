import subprocess
import datetime
import time

while True:
    # Check if the 'spigot' process is running
    pythonProcess = subprocess.check_output("ps aux | grep spigot", shell=True).decode()
    pythonProcess = pythonProcess.split('\n')
    currently_Running = False
    for process in pythonProcess:
        if 'spigot' in process and "grep" not in process:
            currently_Running = True
            good_process = process

    # If 'spigot' process is running
    if currently_Running:
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("[%Y-%m-%d %H:%M:%S]")
        print(f"{formatted_time} Lookin good. It's running: {good_process}")
    else:
        print("Well, it's not running... maybe try restarting?")

        # Restart the 'spigot' process
        try:
            restart_command = "screen -r main && cd /home/zackmartin238/Spigot && ./start.sh"
            subprocess.run(restart_command, shell=True, check=True)
            print("Restarted successfully!")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")

    # Wait for some time before checking again (e.g., 1 minute)
    time.sleep(60)

