import subprocess
import time

# Start the nameserver
nameserver_proc = subprocess.Popen(["pyro5-ns"])

# Start the server
server_proc = subprocess.Popen(["python3", "server.py"])

# Start the client
client_proc = subprocess.Popen(["python3", "client.py"])

try:
    while True:
        time.sleep(1)  # Sleep to keep the main script running
except KeyboardInterrupt:
    # Terminate all subprocesses on Ctrl+C
    nameserver_proc.terminate()
    server_proc.terminate()
    client_proc.terminate()
    print("Exiting gracefully...")
