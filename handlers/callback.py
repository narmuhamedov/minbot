from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from bot_instance import bot

#2
async def games_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Следующая задача', callback_data='next_task2')
    markup.add(button_call_2)
    question = 'Вывод:'
    answers = ['1', '2', '3', 'error']
    photo = open('media/Screenshot_1.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        correct_option_id=1,
        is_anonymous=False,
        type='quiz',
        reply_markup=markup

    )

# 3
async def games_2(call: types.CallbackQuery):
    question = 'Что за соц сеть:'
    answers = ['Google Meet', 'Zoom', 'Telegram', 'error']
    photo = open('media/Screenshot_3.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        correct_option_id=0,
        is_anonymous=False,
        type='quiz',


    )


#Та же самая регистрация что в клиенте только в колбеках
def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(games_1, lambda func: func.data == 'next_task1')
    dp.register_callback_query_handler(games_2, lambda func: func.data == 'next_task2')

