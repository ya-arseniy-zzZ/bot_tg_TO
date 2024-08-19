from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, CallbackContext
import datetime
import json

# Глобальные переменные для хранения выбранных ответственных
responsible_saturday = None
responsible_sunday = None

# Пути к файлу, где хранятся данные об ответственных
responsible_file = "weekend_responsible.json"

def save_weekend_responsible():
    data = {
        "saturday": responsible_saturday,
        "sunday": responsible_sunday
    }
    with open(responsible_file, "w") as file:
        json.dump(data, file)

def load_weekend_responsible():
    global responsible_saturday, responsible_sunday
    try:
        with open(responsible_file, "r") as file:
            data = json.load(file)
            responsible_saturday = data.get("saturday")
            responsible_sunday = data.get("sunday")
    except FileNotFoundError:
        responsible_saturday = None
        responsible_sunday = None

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Я активен и готов к работе!')

async def handle_message(update: Update, context: CallbackContext) -> None:
    global responsible_saturday, responsible_sunday

    text = update.message.text
    today = datetime.datetime.now().weekday()

    if '#ЕГЭ_карточка' in text:
        messages = {
            0: '@shehmatova_um, Аня, помоги, пожалуйста',
            1: '@aglebto, Глеба, ты нам нужен',
            2: '@shehmatova_um, Аня, хелп ми',
            3: '@shehmatova_um, Аня, ты нам нужная',
            4: 'вызываю Глеба, @aglebto',
            5: '@shehmatova_um, Аня, посмотри, пожалуйста, чем можем помочь',
            6: '@shehmatova_um, Аня, буду признателен за твою помощь'}

        day_message = messages.get(today, "Хорошего дня!")
        await update.message.reply_text(day_message)

    if '#трансляция' in text:
        messages = {
            0: '@meva333 и @hobishaker, девочки, нужна ваша помощь',
            1: f'@meva333 и @hobishaker, девочки, мы без вам никуда',
            2: '@meva333 и @hobishaker, Ева, Ксюша, помогите',
            3: '@meva333 и @hobishaker, девочки, есть проблема с трансляциями',
            4: '@meva333 и @hobishaker, вы нам нужны',
            5: f'{responsible_saturday}, хелп-хелп',
            6: f'{responsible_sunday}, без тебя тут никак'
        }

        day_message = messages.get(today, "Хорошего дня!")
        await update.message.reply_text(day_message)


    if '#EГЭ_карточка' in text:
        messages = {
            0: '@shehmatova_um, Аня, помоги, пожалуйста',
            1: '@aglebto, Глеба, ты нам нужен',
            2: '@shehmatova_um, Аня, хелп ми',
            3: '@shehmatova_um, Аня, ты нам нужная',
            4: 'вызываю Глеба, @aglebto',
            5: '@shehmatova_um, Аня, посмотри, пожалуйста, чем можем помочь',
            6: '@shehmatova_um, Аня, буду признателен за твою помощь'}

        day_message = messages.get(today, "Хорошего дня!")
        await update.message.reply_text(day_message)

    # if '#трансляция_запись' in text:
    #     messages = {
    #         0: '@meva333 и @hobishaker, девочки, нужна ваша помощь',
    #         1: f'@meva333 и @hobishaker, девочки, мы без вам никуда',
    #         2: '@meva333 и @hobishaker, Ева, Ксюша, помогите',
    #         3: '@meva333 и @hobishaker, девочки, есть проблема с трансляциями',
    #         4: '@meva333 и @hobishaker, вы нам нужны',
    #         5: f'{responsible_saturday}, хелп-хелп',
    #         6: f'{responsible_sunday}, без тебя тут никак'
    #     }
    #
    #     day_message = messages.get(today, "Хорошего дня!")
    #     await update.message.reply_text(day_message)

    if '#ОГЭ_карточка' in text:
        messages = {
            0: '@haiviro, Виталя, посмотри, пожалуйста, в чем дело',
            1: '@haiviro, Виталя, хелп-хелп',
            2: '@haiviro, Виталя, выручи, пожалуйста',
            3: '@haiviro, Виталь, надо помочь',
            4: '@haiviro, помощь нужна твоя',
            5: '@hobishaker, Ксюша, глянь, пожалуйста, контентный запросик',
            6: 'Вызываю Виталика, @haiviro...'}

        day_message = messages.get(today, "Хорошего дня!")
        await update.message.reply_text(day_message)

    if '10класс_карточка' in text:
        messages = {
            0: '@kostya_axenovum, Костя, нужна помощь с карточкой',
            1: '@kostya_axenovum, Костя, без тебя тут никак',
            2: 'Призываю на помощь Костю, @kostya_axenovum',
            3: '@kostya_axenovum, Костя, посмотри, пожалуйста,  в чем тут дело',
            4: '@umtasha, Наташа, нужна твоя помощь',
            5: '@kostya_axenovum, Костя, помоги, пожалуйста',
            6: '@kostya_axenovum, Костя, ты нам нужен'}

        day_message = messages.get(today, "Хорошего дня!")
        await update.message.reply_text(day_message)

    if '#Средняя_школа_карточка' in text:
        messages = {
            0: '@zilya_krmv, Зиля, ты нам нужна',
            1: '@zilya_krmv, Зиля, нужна твоя помощь',
            2: '@zilya_krmv, Зиля, посмотри, пожалуйста, что тут',
            3: '@zilya_krmv, Зиля, хелп',
            4: '@zilya_krmv, Зиля, тут проблемка',
            5: '@meva333, Ева, тут возник вопросик',
            6: '@zilya_krmv, Зиля, помоги разобаться с ситуацией'
        }

        day_message = messages.get(today, "Хорошего дня!")
        await update.message.reply_text(day_message)

    if '#Трансляция_запись' in text:
        messages = {
            0: '@meva333 и @hobishaker, девочки, нужна ваша помощь',
            1: f'@meva333 и @hobishaker, девочки, мы без вам никуда',
            2: '@meva333 и @hobishaker, Ева, Ксюша, помогите',
            3: '@meva333 и @hobishaker, девочки, есть проблема с трансляциями',
            4: '@meva333 и @hobishaker, вы нам нужны',
            5: f'{responsible_saturday}, хелп-хелп',
            6: f'{responsible_sunday}, без тебя тут никак'
        }

        day_message = messages.get(today, "Хорошего дня!")
        await update.message.reply_text(day_message)

    if '#Общая_проблема' in text:
        messages = {
            0: 'Вызываю Арсения, @ya_arseniy_zzZ...',
            1: 'Вызываю Арсения, @ya_arseniy_zzZ...',
            2: 'Вызываю Арсения, @ya_arseniy_zzZ...',
            3: 'Вызываю Арсения, @ya_arseniy_zzZ...',
            4: 'Вызываю Арсения, @ya_arseniy_zzZ...',
            5: 'Вызываю Арсения, @ya_arseniy_zzZ...',
            6: 'Вызываю Арсения, @ya_arseniy_zzZ...'
        }

        day_message = messages.get(today, "Хорошего дня!")
        await update.message.reply_text(day_message)

    if '#ОБС' in text:
        messages = {
            0: '@AlbertRohov, Альберт, нам нужна твоя помощь! Посмотри, пожалуйста, что можно сделать',
            1: '@AlbertRohov, Альберт, нам нужна твоя помощь! Посмотри, пожалуйста, что можно сделать',
            2: '@AlbertRohov, Альберт, нам нужна твоя помощь! Посмотри, пожалуйста, что можно сделать',
            3: '@AlbertRohov, Альберт, нам нужна твоя помощь! Посмотри, пожалуйста, что можно сделать',
            4: '@AlbertRohov, Альберт, нам нужна твоя помощь! Посмотри, пожалуйста, что можно сделать',
            5: '@AlbertRohov, Альберт, нам нужна твоя помощь! Посмотри, пожалуйста, что можно сделать',
            6: '@AlbertRohov, Альберт, нам нужна твоя помощь! Посмотри, пожалуйста, что можно сделать'
        }

        day_message = messages.get(today, "Хорошего дня!")
        await update.message.reply_text(day_message)

async def weekend_responsible(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("@meva333", callback_data="saturday_meva333"),
            InlineKeyboardButton("@hobishaker", callback_data="saturday_hobishaker")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Кто будет ответственен за трансляции в субботу?",
                                    reply_markup=reply_markup)

async def button_callback(update: Update, context: CallbackContext) -> None:
    global responsible_saturday, responsible_sunday

    query = update.callback_query
    query_data = query.data

    # Выбор ответственного за субботу
    if query_data == "saturday_meva333":
        responsible_saturday = "@meva333"
    elif query_data == "saturday_hobishaker":
        responsible_saturday = "@hobishaker"

    # После выбора ответственного за субботу переходим к воскресенью
    if query_data.startswith("saturday_"):
        keyboard = [
            [
                InlineKeyboardButton("@meva333", callback_data="sunday_meva333"),
                InlineKeyboardButton("@hobishaker", callback_data="sunday_hobishaker")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Кто будет ответственен за трансляции в воскресенье?",
                                      reply_markup=reply_markup)

    # Выбор ответственного за воскресенье
    elif query_data == "sunday_meva333":
        responsible_sunday = "@meva333"
    elif query_data == "sunday_hobishaker":
        responsible_sunday = "@hobishaker"

    # Обновление сообщений для 5 и 6 дня недели после окончательного выбора
    if query_data.startswith("sunday_"):
        final_message = f'В субботу ответственная - {responsible_saturday}'
        final_message_6 = f'В воскресенье ответственная - {responsible_sunday}'
        await query.edit_message_text("Ответственные выбраны.")
        await query.answer()  # Отправка уведомления пользователю, что запрос обработан
        await context.bot.send_message(chat_id=query.message.chat_id, text=final_message)
        await context.bot.send_message(chat_id=query.message.chat_id, text=final_message_6)

        # Сохранение выбранных ответственных в файл
        save_weekend_responsible()

def main():
    # Загрузите предыдущие значения ответственных, если они есть
    load_weekend_responsible()

    TOKEN = '6680569737:AAE91Gy2sDszEQMYMajstuVZDuxppFQH1GU'
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("weekend_responsible", weekend_responsible))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
