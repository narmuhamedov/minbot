from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot_instance import dp, bot


class FSMADMIN(StatesGroup):
    photo = State()
    title = State()
    description = State()


async def is_admin_func(message: types.Message):
    global ADMIN_ID
    ADMIN_ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Радомир какие ваши действия?')


async def fsm_start(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await FSMADMIN.photo.set()
        await message.reply('Радомир отправь мне фото')


async def load_photo(message: types.Message, state:FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMADMIN.next()
        await message.reply('Радомир отправь заголовок к фотке')


#фаза к описанию фотки
async def load_title(message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy()as data:
            data['title'] = message.text
        await FSMADMIN.next()
        await message.reply('Радомир отправь описание к фотке')


#Фаза description
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data['description'] = message.text
        async with state.proxy()as data:
            await message.reply(str(data))
        await state.finish()


def register_handler_fsmadmin(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['download'])
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMADMIN.photo)
    dp.register_message_handler(load_title, state=FSMADMIN.title)
    dp.register_message_handler(load_description, state=FSMADMIN.description)
    dp.register_message_handler(is_admin_func, commands=['admin'], is_chat_admin=True)





