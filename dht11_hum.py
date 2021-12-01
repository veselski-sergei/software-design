#!/usr/bin/env python
# -*- coding: utf-8 -*-
#project: poly-smart-home.ru
import smbus
import time

bus = smbus.SMBus(1)
bus.write_byte(0x40, 0xF5)
time.sleep(0.3)
data0 = bus.read_byte(0x40)
data1 = bus.read_byte(0x40)
humidity = ((data0 * 256 + data1) * 125 / 65536.0) - 6
time.sleep(0.3)
bus.write_byte(0x40, 0xF3)
time.sleep(0.3)
data0 = bus.read_byte(0x40)
data1 = bus.read_byte(0x40)
cTemp = ((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85
print "%.2f" %humidity
