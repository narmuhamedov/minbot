from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_start = KeyboardButton('/start')
button_quiz = KeyboardButton('/quiz')
button_tasks = KeyboardButton('/tasks')
button_location = KeyboardButton('Share Location', request_location=True)
button_info = KeyboardButton('Share Info', request_contact=True)

keyboard_stat = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_stat.row(button_start, button_quiz, button_tasks, button_location, button_info)