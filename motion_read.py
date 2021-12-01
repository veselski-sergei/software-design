#!/usr/bin python
# -*- coding: utf-8 -*-
#project: poly-smart-home.ru
import subprocess
import RPi.GPIO as GPIO

def RCtime (RCpin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RCpin, GPIO.IN)
#       GPIO.wait_for_edge(RCpin,GPIO.FALLING) #можете поиграть с этими строками, оставив 1 нужную
        GPIO.wait_for_edge(RCpin,GPIO.RISING)  #можете поиграть с этими строками, оставив 1 нужную
#       GPIO.wait_for_edge(RCpin,GPIO.BOTH)    #можете поиграть с этими строками, оставив 1 нужную
        signal = GPIO.input(RCpin)
        print "обнаружено движение"

RCtime(16)
