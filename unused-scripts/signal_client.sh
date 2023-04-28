#!/bin/bash

# Read the process ID from the file
pid=$(cat ./var/signal_server.pid)

# Send a signal to the process
kill -SIGUSR1 $pid
