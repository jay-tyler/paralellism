# Much of this code follows verbatim after David Beazley's excellent "Concurrency from the Ground Up"
# https://www.youtube.com/watch?v=MCs5OvhV9S4
# Please refer to David's terms of license; the MIT license might not apply to this code

# perf1.py
# Time of a long running reques

from socket import *
import time

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 20000))

while True:
    start = time.time()
    sock.send(b'30')
    resp = sock.recv(100)
    end = time.time()
    print(end - start)