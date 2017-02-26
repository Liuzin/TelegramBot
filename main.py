import telebot
import constants
import re
import datetime

bot = telebot.TeleBot(constants.token)

#bot.send_message(60649864, "Привет")

#upd = bot.get_updates()
#print(upd)

#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)



@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("Какая неделя", "Расписание")
    user_markup.row("/start", "/help")
    bot.send_message(message.from_user.id, "Ну привет с:", reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handler_text(message):
    if message.text == "Какая неделя":
        if (constants.week[1] % 2) == 0:
            bot.send_message(message.from_user.id, "Нижняя")
        elif (constants.week[1] % 2) == 1:
            bot.send_message(message.from_user.id, "Верхняя")
    if (message.text == "Расписание") and ((constants.week[1] % 2) == 1):
        if constants.weekday == 0:
            bot.send_message(message.from_user.id, "9:45-11:20 ТОЛЬКО ВТОРАЯ ГРУППА Инженерная и компьютерная графика (323) \n"
                                                   "11:30-13:05 Программирование (322) \n"
                                                   "13:30-15:05 ТОЛЬКО ПЕРВАЯ ГРУППА Программирование (308)")
        if constants.weekday == 1:
            bot.send_message(message.from_user.id, "9:45-11:20 ПЕРВАЯ ГРУППА Инженерная и компьютерная графика (323) \n"
                                                    "ВТОРАЯ ГРУППА Программирование (309) \n"
                                                    "9:45-11:20 Инженерная и компьютерная графика (323) \n"
                                                    "11:30-13:05 Технологии дистанционного обучения \n"
                                                    "13:30-15:05 ТОЛЬКО ПЕРВАЯ ГРУППА Технологии дистанционного обучения (309)")
        if constants.weekday == 2:
            bot.send_message(message.from_user.id, "8:00-9:35 Электротехника, электроника и схемотехника (50) \n"
                                                   "9:45-11:20 Электротехника, электроника и схемотехника (44) \n"
                                                   "11:30-13:05 ТОЛЬКО ПЕРВАЯ ГРУППА Электротехника, электроника и схемотехника (260) \n"
                                                   "13:30-16:45 Физическая культура (1)")
        if constants.weekday == 3:
            bot.send_message(message.from_user.id, "11:30-13:05 Защита информации (237) \n"
                                                   "13:30-15:05 ТОЛЬКО ПЕРВАЯ ГРУППА Защита информации (267) \n"
                                                   "15:10-16:45 ПЕРВАЯ ГРУППА Защита информации (267) \n"
                                                   "ВТОРАЯ ГРУППА Прикладные информационные технологии (323) \n"
                                                   "16:50-18:25 Прикладные информационные технологии (323)")
        if constants.weekday == 4:
            bot.send_message(message.from_user.id, "9:45-11:20 ТОЛЬКО ВТОРАЯ ГРУППА Инностранный язык (14) \n"
                                                   "11:30-13:05 ТОЛЬКО ВТОРАЯ ГРУППА Инностранный язык (14) \n"
                                                   "13:30-15:05 Инностранный язык (14) \n"
                                                   "15:10-16:45 ТОЛЬКО ПЕРВАЯ ГРУППА Инностранный язык (14)")
        if constants.weekday == 5:
            bot.send_message(message.from_user.id, "(С 25.03) 9:45-11:20 Менеджмент организации (335) \n"
                                                   "(C 1.04) 11:30-13:05 Менеджмент организации (335) \n"
                                                   "(C 25.03) 13:30-15:05 Менеджмент организации (335)")
        if constants.weekday == 6:
            bot.send_message(message.from_user.id, "Выходной (ориентирование)")
    if (message.text == "Расписание") and ((constants.week[1] % 2) == 0):
        if constants.weekday == 0:
            bot.send_message(message.from_user.id,
                                 "9:45-11:20 ТОЛЬКО ВТОРАЯ ГРУППА Инженерная и компьютерная графика (323) \n"
                                 "11:30-13:05 Программирование (322) \n"
                                 "13:30-15:05 ТОЛЬКО ПЕРВАЯ ГРУППА Программирование (308)")
        if constants.weekday == 1:
            bot.send_message(message.from_user.id,
                                 "9:45-11:20 ПЕРВАЯ ГРУППА Инженерная и компьютерная графика (323) \n"
                                 "ВТОРАЯ ГРУППА Программирование (309) \n"
                                 "9:45-11:20 Инженерная и компьютерная графика (323) \n"
                                 "11:30-13:05 Технологии дистанционного обучения \n"
                                 "13:30-15:05 ТОЛЬКО ВТОРАЯ ГРУППА Технологии дистанционного обучения (309)")
        if constants.weekday == 2:
            bot.send_message(message.from_user.id, "8:00-9:35 Электротехника, электроника и схемотехника (50) \n"
                                                       "9:45-11:20 Электротехника, электроника и схемотехника (44) \n"
                                                       "11:30-13:05 ТОЛЬКО ВТОРАЯ ГРУППА Электротехника, электроника и схемотехника (260) \n"
                                                       "13:30-16:45 Физическая культура (1)")
        if constants.weekday == 3:
            bot.send_message(message.from_user.id, "13:30-15:05 ТОЛЬКО ВТОРАЯ ГРУППА Защита информации (267) \n"
                                                    "15:10-16:45 ПЕРВАЯ ГРУППА Прикладные информационные технологии (323) \n"
                                                    "ВТОРАЯ ГРУППА Защита информации (267) \n"
                                                    "16:50-18:25 Прикладные информационные технологии (323)")
        if constants.weekday == 4:
            bot.send_message(message.from_user.id, "9:45-11:20 ТОЛЬКО ВТОРАЯ ГРУППА Инностранный язык (14) \n"
                                                       "11:30-13:05 ТОЛЬКО ВТОРАЯ ГРУППА Инностранный язык (14) \n"
                                                       "13:30-15:05 Инностранный язык (14) \n"
                                                       "15:10-16:45 ТОЛЬКО ПЕРВАЯ ГРУППА Инностранный язык (14)")
        if constants.weekday == 5:
            bot.send_message(message.from_user.id, "(С 25.03) 9:45-11:20 Менеджмент организации (335) \n"
                                                    "(C 8.04) 11:30-13:05 Менеджмент организации (335) \n"
                                                    "(C 25.03) 13:30-15:05 Менеджмент организации (335)")
        if constants.weekday == 6:
            bot.send_message(message.from_user.id, "Выходной (ориентирование)")
    if message.text == "/help":
            bot.send_message(message.from_user.id,
                             "Чтобы узнать расписание на сегодня - нажми на кнопочку \"расписание\" \n"
                             "Чтобы узнать, какая сейчас неделя - нажми на кнопочку \"неделя\" \n"
                             "Все довльно просто, странно, что ты программист и не понял принцип работы :D")
    if message.text == "id":
            bot.send_message(message.chat.id, "ID = " + str(message.from_user.id))
    if (constants.id == message.from_user.id) and (len(message.text) < 10) and (constants.lol > 3):
        bot.send_message(message.chat.id, "ЗАБАНЕН " + message.from_user.first_name)
        bot.kick_chat_member(message.chat.id, message.from_user.id)
        bot.unban_chat_member(message.chat.id, message.from_user.id)
        constants.lol = 1
    if (constants.id == message.from_user.id) and (len(message.text) < 10):
        bot.send_message(message.chat.id, "Разговаривай не здесь, " + message.from_user.first_name)
        constants.lol += 1
    if (constants.id == message.from_user.id):
        constants.lol += 1
    constants.id = message.from_user.id
    constants.lol += 1

@bot.message_handler(content_types=['voice'])
def handler_voice(message):
    bot.send_message(message.chat.id, "Разговаривай в другом месте, " + message.from_user.first_name)
    bot.kick_chat_member(message.chat.id, message.from_user.id)
    bot.unban_chat_member(message.chat.id, message.from_user.id)


@bot.message_handler(content_types=['audio'])
def handler_audio(message):
    bot.send_message(message.chat.id, "Послушай один и не здесь" + message.from_user.first_name)
    bot.kick_chat_member(message.chat.id, message.from_user.id)
    bot.unban_chat_member(message.chat.id, message.from_user.id)


"""@bot.message_handler(content_types=['sticker'])
def handler_sticker(message):
    if constants.i == 1 and (message.from_user.id == constants.id):
        bot.send_message(message.chat.id, "ПАМ " + message.from_user.first_name)
        #bot.kick_chat_member(message.chat.id, message.from_user.id)
        #bot.unban_chat_member(message.chat.id, message.from_user.id)
        constants.i = 0
    if constants.i > 1:
        constants.i = 0
    constants.i += 1
    constants.id = message.from_user.id
    bot.send_message(message.chat.id, "Меньше стикеров, пожалуйста, " + message.from_user.first_name)
"""

@bot.message_handler(content_types=['sticker'])
def handler_sticker(message):
    if constants.ind == message.from_user.id:
        bot.send_message(message.chat.id, "ЗАБАНЕН " + message.from_user.first_name)
        bot.kick_chat_member(message.chat.id, message.from_user.id)
        bot.unban_chat_member(message.chat.id, message.from_user.id)
    constants.ind = message.from_user.id
    bot.send_message(message.chat.id, "Меньше стикеров, пожалуйста, " + message.from_user.first_name)


bot.polling(none_stop=True)
