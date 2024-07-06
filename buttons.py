from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Moshina sotish")]
    ],
    resize_keyboard=True
)
share_contact = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Telefon raqamini ulashish", request_contact=True)],
        [KeyboardButton(text="Menyuga qaytish")]
    ],
    resize_keyboard=True
)
back = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Menyuga qaytish")]
    ],
    resize_keyboard=True
)

yes_no = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ha"),
         KeyboardButton(text="Yo'q")]
    ],
    resize_keyboard=True
)
