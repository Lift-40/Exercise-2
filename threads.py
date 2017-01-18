# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 14:59:50 2017

@author: César Gutiérrez
"""

import threading
from threading import Thread

shared_var = 0
lock = threading.Lock()

def func1():
    count = 0
    global shared_var
    while count < 999999:
        lock.acquire()
        shared_var += 1
        lock.release()
        count += 1
      
      
def func2():
    count = 0
    global shared_var
    while count < 1000000:
        lock.acquire()
        shared_var -= 1
        lock.release()
        count += 1

def main():
    global shared_var
    thread1 = Thread(target = func1, args = ())
    thread2 = Thread(target = func2, args = ())
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print "shared_var = %d" % shared_var

main()