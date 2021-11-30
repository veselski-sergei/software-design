#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
#project: poly-smart-home.ru

import sys,os

# считывание температуры из скрипта для dht11
def temp_read():
	return 1.0

# считывание влажности из скрипта для dht11
def hum_read():
        return 1.0

# считывание значения с датчика воды
def water_read():
	return "abc"

# считывание состояния пина на котором висит реле
def relay_read():
	return "abc"

# включение/выключение реле в зависимости от входящего параметра
def relay_execute(state):
	return "abc"

# управление сигнализациями alarm: on/off. file_id - айдишник сигнализации (см выше)
def alert_f(alarm, file_id):
	return "abc"

# текущее сотояние сигнализации. file_id - айдишник сигнализации (см выше)
def alert_info_f(file_id):
	return "abc"

# Текущее минимальное значение температуры
# считывание значения с датчика воды
def c_t_read():
	return "abc"
