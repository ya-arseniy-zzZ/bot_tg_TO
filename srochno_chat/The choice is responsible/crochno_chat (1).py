import schedule
import time
from telegram import Bot
import asyncio
from datetime import datetime
import json

# Токен, который вы получили от BotFather
TOKEN = '6680569737:AAE91Gy2sDszEQMYMajstuVZDuxppFQH1GU'
bot = Bot(TOKEN)

# ID чата, куда бот будет отправлять сообщения
chat_id = '-1001949124952'

# Пути к файлу с ответственными лицами
responsible_file = "weekend_responsible.json"

# Словарь сообщений с заполнителями для ответственных лиц
messages = {
    'Monday': ('Чат срочных запросов открыт!\n\nВсем привет! Понедельник день тяжелый, но не переживайте, чат срочные здесь, чтобы облегчить вашу неделю. Помните, даже самая длинная неделя начинается с первого дня! 😊🌟\n\nРаспределение сегодня такое:\n\nВопросы по карточкам:\n\n🌟 ЕГЭ - Аня (@shehmatova_um)\n🌟 ОГЭ - Виталий (@haiviro)\n🌟10 класс - Костя (@kostya_axenovum)\n🌟 Средняя школа - Зиля (@zilya_krmv)\n\nВопросы по трансляциям:\n\n😊 Ева (@meva333)\n😊 Ксюша (@hobishaker)'),
    'Tuesday': ('Чат срочных запросов открыт!\n\nСчастливого вторника! Если бы понедельник был фильмом, вторник точно бы стал его сиквелом. Не забудьте заглянуть в чат срочные за ежедневной дозой поддержки! 🎬🍿\n\nРаспределение сегодня такое:\n\nВопросы по карточкам:\n\n🎬 ЕГЭ - Глеб (@aglebto)\n🎬 ОГЭ - Виталий (@haiviro)\n🎬 10 класс - Костя (@kostya_axenovum)\n🎬 Средняя школа - Зиля (@zilya_krmv)\n\nВопросы по трансляциям:\n\n🍿 Ева (@meva333)\n🍿 Ксюша (@hobishaker)'),
    'Wednesday': ('Чат срочных запросов открыт!\n\nПривет всем! Среда - это маленькая пятница, а чат срочные - ваш личный антистресс. Давайте сделаем этот день на удивление легким! 🌈😉\n\nРаспределение сегодня такое:\n\nВопросы по карточкам:\n\n🌈 ЕГЭ - Аня (@shehmatova_um)\n🌈 ОГЭ - Виталий (@haiviro)\n🌈 10 класс - Костя (@kostya_axenovum)\n🌈 Средняя школа - Зиля (@zilya_krmv)\n\nВопросы по трансляциям:\n\n😉 Ева (@meva333)\n😉 Ксюша (@hobishaker)'),
    'Thursday': ('Чат срочных запросов открыт!\n\nЗдравствуйте в четверг! Помните, что после четверга уже практически пятница. А пока что, чат срочные поможет вам оставаться на плаву. ⛵💪\n\nРаспределение сегодня такое:\n\nВопросы по карточкам:\n\n⛵ ЕГЭ - Аня (@shehmatova_um)\n⛵ ОГЭ - Виталий (@haiviro)\n⛵10 класс - Костя (@kostya_axenovum)\n⛵ Средняя школа - Зиля (@zilya_krmv)\n\nВопросы по трансляциям:\n\n💪 Ева (@meva333)\n💪 Ксюша (@hobishaker)'),
    'Friday': ('Чат срочных запросов открыт!\n\nУра, пятница! Время начинать отсчет до выходных. А пока что чат срочные поможет вам закончить рабочую неделю на высокой ноте! 🎉🕺\n\nРаспределение сегодня такое:\n\nВопросы по карточкам:\n\n🎉 ЕГЭ - Глеб (@aglebto)\n🎉 ОГЭ - Виталий (@haiviro)\n🎉 10 класс - Наташа (@umtasha)\n🎉 Средняя школа - Зиля (@zilya_krmv)\n\nВопросы по трансляциям:\n\n🕺 Ева (@meva333)\n\n🕺 Ксюша (@hobishaker)'),
    'Saturday': ('Чат срочных запросов открыт!\n\nСуббота настала, и даже если вы на работе, чат срочные здесь, чтобы добавить немного веселья в ваш выходной. Работа или отдых - мы поддержим вас! 🎈😃Распределение сегодня такое:\n\nВопросы по карточкам:\n\n🎈 ЕГЭ - Аня (@shehmatova_um)\n🎈 ОГЭ - Ксюша (@hobishaker)\n🎈 10 класс - Костя (@kostya_axenovum)\n🎈 Средняя школа - Соня (@umschsonia)\n\nВопросы по трансляциям:\n\n😃 {responsible_saturday}'),
    'Sunday': ('Чат срочных запросов открыт!\n\nПривет в воскресенье! День для отдыха, но если вам нужно что-то срочное, чат всегда на связи. Пусть это воскресенье будет мягким как ваше любимое одеяло. 😴🛋️\n\nРаспределение сегодня такое:\n\nВопросы по карточкам:\n\n😴 ЕГЭ - Аня (@shehmatova_um)\n😴 ОГЭ - Виталий (@haiviro)\n😴 10 класс - Костя (@kostya_axenovum)\n😴 Средняя школа - Зиля (@zilya_krmv)\n\nВопросы по трансляциям:\n\n🛋 {responsible_sunday}')
}


# Функция загрузки ответственных лиц из JSON-файла
def load_weekend_responsible():
    try:
        with open(responsible_file, "r") as file:
            data = json.load(file)
            return data.get("saturday", None), data.get("sunday", None)
    except FileNotFoundError:
        return None, None


# Функция отправки сообщения с актуальными ответственными
async def send_message(message):
    await bot.send_message(chat_id=chat_id, text=message)


# Задача отправки сообщения с обновленными ответственными лицами
def job():
    # Получаем текущий день недели
    day_of_week = datetime.now().strftime('%A')

    # Загружаем ответственных лиц из файла
    responsible_saturday, responsible_sunday = load_weekend_responsible()

    # Исходное сообщение с заполнителями
    message_template = messages.get(day_of_week, "Сегодня хороший день!")

    # Подставляем ответственных в сообщение с использованием метода .format()
    message = message_template.format(
        responsible_saturday=responsible_saturday or "неизвестно",
        responsible_sunday=responsible_sunday or "неизвестно"
    )

    # Отправляем соответствующее сообщение
    asyncio.run(send_message(message))


# Запланировать задачу на отправку сообщений каждый день в 10:00
schedule.every().day.at("10:00").do(job)

# Запуск планировщика в бесконечном цикле
while True:
    schedule.run_pending()
    time.sleep(60)
