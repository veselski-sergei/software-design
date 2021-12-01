#!/usr/bin/env python
# -*- coding: utf-8 -*-
#project: poly-smart-home.ru
import RPi.GPIO as io

pin=17 #сигнальный провод от датчика воды идет на 17 pin

io.setmode(io.BCM)
io.setup(pin, io.IN)         #устанавливаем пин на вход
signal = io.input(pin)       #считываем сигнал
if signal == 1:
    print "датчик сухой"
elif signal == 0:
    print "на датчике обнаружена вода!"
else:
    print "ошибка!"
