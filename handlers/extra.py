from aiogram import types, Dispatcher
from bot_instance import bot




#Кости
#Удаляет матерные слова
async def echo_and_ban(message: types.Message):
    ban_words = ['bitch', 'slut', 'java', 'python is bad']
    for i in ban_words:
        if i in message.text.lower().replace(" ", ""):
            await message.delete()
            await bot.send_message(message.chat.id, "Вы забанены за плохие слова!!!")
    #Игра в кости
    if message.text.lower() == 'dice':
        await bot.send_dice(message.chat.id, emoji='🎲')

    if message.text.lower()in ban_words:
        await message.reply('Это слово плохое Бот админ его удалил!!!')
        await bot.delete_message(message.chat.id, message.message_id)


async def secret_word1(message: types.Message):
    await message.reply('Cижу на паре ты что? !!!')

async def secret_word2(message: types.Message):
    await message.reply('Все понятно!')

async def secret_word3(message: types.Message):
    await message.reply('Мне скучно')


#echo bot
# @dp.message_handler()
# async def echo_message(message: types.Message):
#     await message.answer(message.text)
def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(secret_word1, lambda word: "Что делаешь сейчас?".lower() in word.text)  # регистрируем бота ответчика
    dp.register_message_handler(secret_word2,
                                lambda word: "Я тоже".lower() in word.text)  # регистрируем бота ответчика
    dp.register_message_handler(secret_word3, lambda word: 'ааа'.lower() in word.text)

    dp.register_message_handler(echo_and_ban, content_types=['text'])



