from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отмена'))

size_panel = ReplyKeyboardMarkup(resize_keyboard=True,
                                 row_width=2)
(size_panel.add("XXL").add("XL").add("L").add("M").add("S"))

question = ReplyKeyboardMarkup(resize_keyboard=True)
question.add("Да").add("Нет")

submit_buttons = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Да'), KeyboardButton('Нет')
)