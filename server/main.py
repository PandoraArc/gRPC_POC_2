import subprocess
import time
import signal
import os

p1 = subprocess.Popen(['python', 'flask_app.py'])
p2 = subprocess.Popen(['python', 'grpc_server.py'])

try:
    while True:
        print("server is now running")
        time.sleep(5)
except KeyboardInterrupt:
    os.kill(os.getpid(p1.pid), signal.SIGTERM)
    os.kill(os.getpid(p2.pid), signal.SIGTERM)
    print("Kill all processes")