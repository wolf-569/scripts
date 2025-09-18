#!/opt/homebrew/bin/python3
import subprocess
import socket, time, signal, sys, smtplib
from datetime import datetime


HOST = "<ip>"
PORT = 22
INTERVAL = 120

def log(msg):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {msg}")

def signal_handler(sig, frame):
    print('\nBye!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def notify(title, msg):
    subprocess.run([
        "osascript", "-e",
        f'display notification "{msg}" with title "{title}"'
    ])

def check_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        try:
            s.connect((HOST, PORT))
            log(f"Server is up")
        except Exception as e:   
            notify("Helios Status", "Server Down")
            log(f"Server is down {e}")


if __name__ == "__main__":  
    while True:
        check_server()
        time.sleep(INTERVAL)
