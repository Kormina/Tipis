# t.me/sinfi_3_bot

import telebot
from token import token, chatId
from telegram import InputMediaPhoto
import telebot.types

bot = telebot.TeleBot(token)
bot.send_message(chatId, 'Привет', parse_mode='MarkdownV2')
img = open("photo.jpg", 'rb')
bot.send_photo(chatId, img)
audio = open("music.mp3", 'rb')
bot.send_audio(chatId, audio)
video = open("video.mp4", 'rb')
bot.send_video(chatId, video)

bot.polling(none_stop=True)
