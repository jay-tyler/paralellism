# Much of this code follows verbatim after David Beazley's excellent "Concurrency from the Ground Up"
# https://www.youtube.com/watch?v=MCs5OvhV9S4
# Please refer to David's terms of license; the MIT license might not apply to this code

# perf2.py
# Time of fast requests

from socket import *
import time

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 20000))

n = 0

from threading import Thread
def monitor():
    global n
    while True:
        time.sleep(1)
        print(n, 'reqs/second')
        n = 0

Thread(target=monitor).start()

while True:
    sock.send(b'1')
    resp = sock.recv(100)
    n += 1