from telegram import Bot
import asyncio

# Токен, который вы получили от BotFather
TOKEN = '6680569737:AAE91Gy2sDszEQMYMajstuVZDuxppFQH1GU'
bot = Bot(TOKEN)

# ID чата, куда бот будет отправлять сообщения
chat_id = '-4229010801'

async def send_message():
    # Отправка сообщения асинхронно
    await bot.send_message(chat_id=chat_id, text='@meva333, Ева, привет! Выбери ответственных в выходные\n\n Нажми на команду - /weekend_responsible')

# Запуск асинхронной функции
asyncio.run(send_message())