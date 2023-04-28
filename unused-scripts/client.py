import os
import signal
import time

# Read the server PID from the text file
with open('server_pid.txt', 'r') as f:
    server_pid = int(f.read())

# Send a signal to the server process
os.kill(server_pid, signal.SIGUSR1)

# Wait for the server to handle the signal
time.sleep(1)
