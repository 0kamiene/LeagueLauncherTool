import psutil
import ctypes
import os
import sys
import subprocess

# Programs
league_path = r"C:\Riot Games\League of Legends\LeagueClient.exe"
riot_path = r"C:\Riot Games\Riot Client\RiotClientServices.exe"
league_of_legends = f'"{riot_path}" --launch-product=league_of_legends --launch-patchline=live'
lolclient = "LeagueClient.exe"
riotclient = "RiotClientServices.exe"

def check_admin():
    # Check if the script is running with admin privileges
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def is_process_running(task_name):
    # Check if the program is running
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == task_name:
            return True
    return False

def kill_program(process):
    # Terminates a program
    for proc in psutil.process_iter(['name']):
            if proc.info['name'] == process:
                proc.kill()
                return

def run(path, lolpath, league, riot):
    does_exist = os.path.exists(path)
    if not does_exist:
        
        sys.exit()

    if is_process_running(league):
        kill_program(league)
    if is_process_running(riot):
        kill_program(riot)

    # Starts program
    subprocess.Popen(lolpath, shell=True)
    sys.exit()

# Main execution
if __name__ == "__main__":
    if check_admin():
        run(league_path, league_of_legends, lolclient, riotclient)
    else:

        sys.exit()

# pyinstaller --onefile --windowed --icon=riot.ico --uac-admin League_Of_Legends.py