#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Пример работы с таймером

if __name__ == "__main__":
    from threading import Timer
    from time import sleep, time
    timer = Timer(interval=3, function=lambda: print("Message from Timer!"))
    timer.start()