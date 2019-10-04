# python per hour . telegram bot

import pyowm
import telebot

owm = pyowm.OWM('a94912d827ff0f958082238e40144c1f')  # You MUST provide a valid API key
bot = telebot.TeleBot("986374153:AAGwfGbSzz7Zs8M5zTQty0hb_XnrRIBRJas")  # pogodabillbot

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = "Weather condition is ..\nIn city " + message.text + " now is " + w.get_detailed_status() + "\n"
	answer += "ambient temperature now is " + str(temp) + "\nMy recommendations : \n"

	if temp < 10:
		answer += "    - It's cold outside, dress warmly! "
	elif temp < 20:
		answer += "    - It's cool now, dress warmer ;-) "
	else:
		answer += "    - Get warm outside, wear whatever you want :-) "

	bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)

