#!/usr/bin/env python
# -*- coding: utf-8 -*-
#project: poly-smart-home.ru

import time,os
import subprocess
from subprocess import Popen, PIPE
import threading
from threading import Thread

t_s = 3     #штатный интервал ожидания
t_s2 = 30   #аварийный интервал ожидания воды
t_s3 = 30   #повторный интервал ожидания движения
t_s4 = 30   #интервал ожидания после того как температура упала ниже критической

file_path = os.getcwd() #айдишники сигнализаций
                        #cигнализация будет включена или выключена в зависимости от наличия айдишника

water_id = file_path + '/alert_state/w_on'
motion_id = file_path + '/alert_state/m_on'
temper_id = file_path + '/alert_state/t_on'

#проверка воды
class water_check(threading.Thread):
	def run(self):
		while True:
			if(os.path.exists(water_id)):
				proc = Popen(['''/home/pi/Desktop/bot/water_read.py'''], shell=True, stdout=PIPE, stderr=PIPE)
				proc.wait()
				w = proc.communicate()[0]
				w = w.decode(encoding='utf-8')
				w = w.replace('\n','')
				if(w == u'на датчике обнаружена вода!'):
					print w
					text = "Хозяин! Мы тонем! На датчике вода! Проверь скоре"
	                                subprocess.call(['''/home/pi/Desktop/bot/telegram_sender.py "%s"''' %text], shell=True)
					time.sleep(t_s2)
				elif(w == u'датчик сухой'):
					time.sleep(t_s)
				else:
					print("ERR")
					time.sleep(t_s)
			else:
				print('сигналка воды выключена')
				time.sleep(t_s)

water_check().start()

#проверка движения
class motion_check(threading.Thread):
    def run(self):
        while True:
            if(os.path.exists(motion_id)):
                proc = Popen(['''/home/pi/Desktop/bot/motion_read.py'''], shell=True, stdout=PIPE, stderr=PIPE)
                proc.wait()
                m = proc.communicate()[0]
                m = m.decode(encoding='utf-8')
                m = m.replace('\n','')
                if(m == u'обнаружено движение'):
                    print m
                    text = "Хозяин! Кто-то  тут ходит! Это ты? Мне страшно.."
                    subprocess.call(['''/home/pi/Desktop/bot/telegram_sender.py "%s"''' %text], shell=True)
                    time.sleep(t_s3)
                else:
                    print("ERR")
                    time.sleep(t_s)
            else:
                print('сигналка движения выключена')
                time.sleep(t_s)

motion_check().start()

#считывание минимального градуса(целое значение)
def critical_read():
        inf = Popen('''cat /home/pi/Desktop/bot/alert_state/critical_temp''', shell=True, stdout = PIPE)
        inf.wait()
        out = inf.communicate()
        t = out[0].replace("\n", "")
        t = int(t)
        return t

#получение актуальной температуры
def temper_inf():
        txt = file_path + "/dht11_temp.py"
        exe =  Popen("%s" % txt, shell=True, stdout = PIPE)
        exe.wait()
        inf = exe.communicate()
        inf = inf[0].replace("\n","")
        if(inf == ''):
                print('нету результата текущей температуры')
                none = 1000
                return none
        elif(inf == 'None'):
		none = 1000
                print('нету результата текущей температуры')
                return none
        else:
            t = round(float(inf))
            t = int(t)
            return t

#проверка температуры
class temper_check(threading.Thread):
	def run(self):
		while True:
			if(os.path.exists(temper_id)):
				t_now = temper_inf()
				t_critical = critical_read()
				if(t_now == 1000):
					time.sleep(t_s)
				elif(t_now < t_critical):
					info = "Текущая температура: %s C" %t_now
					print(info)
					text = "Хозяин! Температура ниже критической! Я замерзаю...  Текущая температура: %s C" %t_now
					subprocess.call(['''/home/pi/Desktop/bot/telegram_sender.py "%s"''' %text], shell=True)
					time.sleep(t_s4)
				else:
					time.sleep(t_s)
			else:
				time.sleep(t_s)

temper_check().start()
