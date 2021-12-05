#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
#project: poly-smart-home.ru
import sys
import telepot

text = sys.argv[1]
chat_id = 123456789  #меняем
TOKEN = "1234567890:xyyxyxyxyxyyyxyxyxyxyxyyxyxyxyyxyx" #меняем
bot = telepot.Bot(TOKEN)
bot.sendMessage(chat_id, str(text))
