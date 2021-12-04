#!/usr/bin/env python
# -*- coding: utf-8 -*-
#project: poly-smart-home.ru

import time,os
import subprocess
from subprocess import Popen, PIPE
import threading
from threading import Thread

t_s = 3
t_s2 = 30
t_s3 = 30

file_path = os.getcwd()

water_id = file_path + '/alert_state/w_on'
motion_id = file_path + '/alert_state/m_on'

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
					text = "На датчике вода!"
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
                        text = "Кто-то ходит!"
                        subprocess.call(['''/home/pi/Desktop/bot/telegram_sender.py "%s"''' %text], shell=True)
                        time.sleep(t_s3)
                else:
                        print("ERR")
                        time.sleep(t_s)
            else:
                print('сигналка движения выключена')
                time.sleep(t_s)

motion_check().start()
