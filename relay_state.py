#!/usr/bin/env python
# -*- coding: utf-8 -*-
#project: poly-smart-home.ru
import subprocess
from subprocess import Popen, PIPE

pin_number = 20 #пин с сигнальным проводом реле

proc = Popen(
    "echo %s > /sys/class/gpio/export" % pin_number,
    shell=True,
    stdout=PIPE, stderr=PIPE
)
proc.wait()
proc = Popen(
    "cat /sys/class/gpio/gpio%s/value" % pin_number,
    shell=True,
    stdout=PIPE, stderr=PIPE
)
proc.wait()
res = proc.communicate()
count = res[0].replace("\n","")
count = int(count)
if count == 1:
        print('0').replace("\n","")
else:
        print('1').replace("\n","")
