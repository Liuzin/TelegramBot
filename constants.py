import datetime
import re
import telebot

token = "301473800:AAEYtNW6aIF1LdTIT9Eb5Xj_3aqvfGPoiHs"
date = str(datetime.date.today())
l = re.split(r'-', date)
day = int(l.pop())
mouth = int(l.pop())
year = int(l.pop())
week = datetime.date(year, mouth, day).isocalendar()
weekday = datetime.date(year, mouth, day).weekday()
i = 1
id = 0
ind = 0
lol = 0
