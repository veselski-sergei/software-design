#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
#project: poly-smart-home.

import RPi.GPIO as GPIO
import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 16
instance = dht11.DHT11(pin = 16)
result = instance.read()

if result.is_valid():
    print("%-3.1f" % result.humidity)
else:
    print("Error: %d" % result.error_code)
