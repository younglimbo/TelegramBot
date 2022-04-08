import telebot, wikipedia, re
bot = telebot.TeleBot ('5142931930:AAH3Rl8NGk3b79O0G_DOvZNAFb05WZx09xU')

wikipedia.set_lang("ru")

def getwiki(s):
	try:
		ny = wikipedia.page(s)
		#Получаем пурвую тысячу символов
		wikitext=ny.content[:1000]
		#Разделяем по точкам
		wikimas=wikitext.split('.')
		#Отбрасываем всё после последней точки
		wikimas = wikimas[:-1]
		#Создаем пустую переменную текста
		wikitext2 = ''
		#Проходим по строкам, где нет знаков РАВНО (то есть все кроме заголовков)
		for x in wikimas:
			if not('==' in x):
			#Если в строке осталось больше трех символов , добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
				if(len((x.strip()))>3):
					wikitext2=wikitext2+x+'.'
			else:
				break

		# Теперь при помощи регулярных выражений убираем разметку
		wikitext2=re.sub('\([^()]*\)', '', wikitext2)
		wikitext2=re.sub('\([^()]*\)', '', wikitext2)
		wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
		# Возвращаем текстовую строку
		return wikitext2
		# Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
	except Exception as e:
		return 'В энциклопедии нет информации об этом'

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
	bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')	

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
	bot.send_message(message.chat.id, getwiki(message.text))
# Запускаем бота
bot.polling(none_stop=True, interval=0)