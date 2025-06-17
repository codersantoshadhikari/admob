import os
import time
from datetime import datetime

REPO_PATH = os.getcwd()  # Change to your repo path if different
COMMIT_INTERVAL = 1200  # 20 minutes in seconds

def run_system():
    """Run your system code here"""
    with open("system_output.log", "a") as f:
        f.write(f"System ran at {datetime.now()}\n")
    return True

def git_operations():
    os.chdir(REPO_PATH)
    os.system("git add .")
    os.system(f'git commit -m "Auto-commit: {datetime.now()}"')
    os.system("git push origin main")

if __name__ == "__main__":
    print("Auto-Commit System Started")
    while True:
        try:
            if run_system():
                git_operations()
                print(f"Commit successful at {datetime.now()}")
            time.sleep(COMMIT_INTERVAL)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)  # Wait 1 minute before retrying