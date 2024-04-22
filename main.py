import subprocess
import time

nameserver_proc = subprocess.Popen(["pyro5-ns"])

server_proc = subprocess.Popen(["python3", "server.py"])

client_proc = subprocess.Popen(["python3", "client.py"])

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    nameserver_proc.terminate()
    server_proc.terminate()
    client_proc.terminate()
    print("Exiting gracefully...")
