#!/usr/bin/env python
# -*- coding: utf-8 -*-
#project: poly-smart-home.ru
import RPi.GPIO as GPIO

gpio_pin_number=20  #на 20 пине (BCM) сигнальный контакт реле
print("r_off use_pin:" + str(gpio_pin_number))
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(gpio_pin_number, GPIO.OUT)
GPIO.output(gpio_pin_number, GPIO.LOW)
