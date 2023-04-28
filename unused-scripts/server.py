import os
import signal
import time
# Define a signal handler function to receive the signal
def signal_handler(signum, frame):
    message = "Received signal from client"
    print(message)

# Register the signal handler function for SIGUSR1 signals
signal.signal(signal.SIGUSR1, signal_handler)



# Write the server PID to a text file
pid_file = "var/signal_server.pid"
with open(pid_file, 'w') as f:
    f.write(str(os.getpid()))

# Print the server PID for reference
print("Server PID:", os.getpid())

# Wait indefinitely for signals
while 1:
    # print('xxx')
    # signal.pause()
    time.sleep(0.1)
