#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
#project: poly-smart-home.ru

import subprocess
from subprocess import Popen, PIPE
import sys, os

# Ниже пути расположения скриптов чтения значений датчиков и управление реле.
# Каждый файл - исполняемый питоновский скрипт. 
# Необходимо чтобы все файлы были представлены в системе и были исполняемыми.
file_path = os.getcwd()

file_read_temp = file_path + '/dht11_temp.py'
file_read_hum = file_path + '/dht11_hum.py'
file_read_water = file_path + '/water_read.py'
file_read_relay = file_path + '/relay_state.py'
file_relay_on = file_path + '/relay_on.py'
file_relay_off = file_path + '/relay_off.py'

# Блок переменных ниже - блок файлов-индификаторов (просто айдишник), отвечающиx за состояние сигнализации.
# Для них в директории /home/pi создается отдельная директория (/home/pi/alert_state)  
# Если файл сигнализации присутствует - значит сигнализация должна слать алерты при срабатывании.
# Если файл отсутствует значит считаем что сигнализация выключена. Необходимо для перезагрузок (обесточевания)
# И других программ которые хотят знать что с сигнализацией
water_id = file_path + '/alert_state/w_on'
motion_id = file_path + '/alert_state/m_on'
temper_id = file_path + '/alert_state/t_on'

# Файл со значением минимального температурного порога срабатывания температурной сигналки
# файл должен существовать и необходимо внести в него значение температуры (целое число)
critical_temp = file_path + '/alert_state/critical_temp'

# считывание температуры из скрипта для dht11
def temp_read():
	proc = Popen(['%s' %file_read_temp], shell=True, stdout=PIPE, stderr=PIPE)
	proc.wait()
	t = proc.stdout.read()
	t = float(t)
	return t

# считывание влажности из скрипта для dht11
def hum_read():
        proc = Popen(['%s' %file_read_hum], shell=True, stdout=PIPE, stderr=PIPE)
        proc.wait()
        H = proc.stdout.read()
        H = float(H)
        return H

# считывание значения с датчика воды
def water_read():
	proc = Popen(['%s' %file_read_water], shell=True, stdout=PIPE, stderr=PIPE)
	proc.wait()
	w = proc.communicate()[0]
	w = w.decode(encoding='utf-8')
	return w

# считывание состояния пина на котором висит реле
def relay_read():
	proc = Popen(['%s' %file_read_relay], shell=True, stdout=PIPE, stderr=PIPE)
	proc.wait()
	r = proc.communicate()[0]
	r = int(r)
	if(r == 1):
		r = 'Реле включено'
	elif(r == 0):
		r = 'Реле обесточено'
	else:
		r = 'Ошибка!'
	return r

# включение/выключение реле в зависимости от входящего параметра
def relay_execute(state):
	if(state == 'on' and relay_read() == 'Реле обесточено'):
		subprocess.call("%s" %file_relay_on, shell=True)
		text = "включаю реле"
	elif(state == 'on' and relay_read() == 'Реле включено'):
		text = "реле уже под напряжением"
	elif(state == 'off' and relay_read() == 'Реле включено'): 
		subprocess.call("%s" %file_relay_off, shell=True)
		text = "отключаю реле"
	elif(state == 'off' and relay_read() == 'Реле обесточено'):
		text = "реле уже обесточено"
	else:
		print("Ошибка!")
	return text

# управление сигнализациями alarm: on/off. file_id - айдишник сигнализации (см выше)
def alert_f(alarm, file_id):
	#сигнализация уже включена
	if (alarm == 'on' and os.path.exists(file_id)):
		text = "Сигнализация уже была включена"
	#была включена, теперь отключаем
	elif(alarm == 'off' and os.path.exists(file_id)):
		text = "Отключаю сигнализацию"
		subprocess.call("rm -f %s" %file_id, shell=True)
	#уже была выключена, выключать не надо
	elif(alarm == 'off' and os.path.exists(file_id) == False):
		text = "Сигнализация уже была отключена"
	#выла выключена, теперь включаем
	elif(alarm == 'on' and os.path.exists(file_id) == False):
		text = "Активирую сигнализацию"
		subprocess.call("touch %s" %file_id, shell=True)
	else:
		text = "err"
	return text

# текущее сотояние сигнализации. file_id - айдишник сигнализации (см выше)
def alert_info_f(file_id):
	if(os.path.exists(file_id)):
		text = "Сигнализация сейчас активна"
	else:
		text = "Сигнализация сейчас отключена"
	return text

# Текущее минимальное значение температуры
# считывание значения с датчика воды
def c_t_read():
	proc = Popen(['cat %s' %critical_temp], shell=True, stdout=PIPE, stderr=PIPE)
	proc.wait()
	c_t = proc.communicate()[0]
	c_t = c_t.decode(encoding='utf-8')
	c_t = "\nПорог срабатывания установлен на " + c_t + " градусов"
	return c_t
