import telebot
from telebot import types
import database
import checker


bot = telebot.TeleBot('5574416924:AAE2BXF5lMpHhF7KsyWQveR0fRBsfq5Q-u4')


@bot.message_handler(commands=['start'])
def start(message):
    # создаем тело клавиатуры
    markup = types.InlineKeyboardMarkup(row_width=1)

    # создание самих кнопок
    item1 = types.InlineKeyboardButton("История заявок", callback_data='back')
    item2 = types.InlineKeyboardButton("Обо мне", callback_data='contacts')

    # Добавление кнопок в тело клавиатуры
    markup.add(item1, item2)

    mess = f'Привет, {message.from_user.first_name}!!!\nЯ - Народная тропа и я веду туда, куда тебе захочется :)'
    hi_photo = open('folk.jpg', "rb")
    bot.send_photo(message.chat.id, hi_photo, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['h'])
def get_history(message):
    history_list = database.get_user_history(message.chat.id)
    print(history_list)
    if history_list:
        text = "История поиска:\n"
        history_list.reverse()
        for i in range(len(history_list)):
            text += '{}. {}\n'.format(i + 1, history_list[i])
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, "Вы пока ничего не искали")


@bot.callback_query_handler(func=lambda call: True) #назначение кнопок
def callback_inline(call):
    markup1 = types.InlineKeyboardMarkup(row_width=1)
    markup2 = types.InlineKeyboardMarkup(row_width=1)

    item1 = types.InlineKeyboardButton("История заявок", callback_data='back')
    item2 = types.InlineKeyboardButton("Обо мне", callback_data='contacts')

    markup1.add(item1)
    markup2.add(item2)
    try:
        if call.message:
            if call.message:
                if call.data == 'contacts':
                    bot.answer_callback_query(call.id)
                    sti = open("svyaz.jpg", 'rb')
                    bot.send_photo(call.message.chat.id, sti)
                    bot.send_message(call.message.chat.id, f'Что ж, что я могу тебе рассказать обо мне,{call.message.from_user.first_name}, это, конечно, большойй вопрос\n\n'
                                                           'Смысл моего существования - это облегчение твоей жизни. Я даю возможность зайти туда куда ты захочешь просто используя ссылку...\n\n'
                                                           'Поэтому пользуйся, мне все это только в радость!\n\nРазработчик: <i><b>Livanoff</b></i>\nE-MAIL', parse_mode='html', reply_markup=markup1)

                    #Тут реализуем вывод списка предыдущих запросов
                elif call.data == 'back':
                    bot.answer_callback_query(call.id)
                    history_list = database.get_user_history(call.message.chat.id)
                    if not history_list:
                        bot.send_message(call.message.chat.id, "Вы пока ничего не искали")
                    else:
                        text = "История поиска:\n"
                        history_list.reverse()
                        for i in range(len(history_list)):
                            text += '{}. {}\n'.format(i+1, history_list[i])
                        bot.send_message(call.message.chat.id, text)
    except Exception as e:
        print(repr(e))


@bot.message_handler(content_types=['text'])
def get_workaround_website(message):
    answer = checker.url_data_check(message.text)
    if answer == 0:
        bot.send_message(message.chat.id, "Нет возможности получить доступ к сайту. Проверьте введенные данные.")
    else:
        database.insert_url_in_user_history(message.chat.id, message.text)
        bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
