# imports ________________________________________________________
# aiogram
from aiogram import Router, F
# aiogram filters
from aiogram.filters import Command
# aiogram fsm context
from aiogram.fsm.context import FSMContext
# aiogram types
from aiogram.types import Message

# bot
from bot import bot
from config import ADMIN
# db
from db import add_movie_db, check_movie
# states
from states import states

# settings _______________________________________________________

# router
router = Router()


# handlers _______________________________________________________

# admin

@router.message(Command('add'), F.from_user.id.in_(ADMIN))
async def add_movie(message: Message, state: FSMContext):
    await message.answer('Kinoning kodini yozing')
    await state.set_state(states.kod)


@router.message(F.text.isdigit() & ~F.text.startswith('0'), states.kod)
async def code(message: Message, state: FSMContext):
    if check_movie(movie_id=int(message.text)):
        await message.answer('Bunaqa kodli kino allaqachon mavjud, iltimos boshqa kod yozing')
    else:
        await message.answer('Kinoning nomini yozing')
        await state.set_state(states.nomi)

        await state.update_data({'code': message.text})


@router.message(F.text, states.nomi, F.from_user.id.in_(ADMIN))
async def quality(message: Message, state: FSMContext):
    await message.answer('Kinoning kechestovasini yozing')
    await state.set_state(states.quality)

    await state.update_data({'name': message.text})


@router.message(F.text, states.quality, F.from_user.id.in_(ADMIN))
async def video(message: Message, state: FSMContext):
    await message.answer('Kinoni yuboring')
    await state.set_state(states.video)

    await state.update_data({'quality': message.text})


@router.message(F.video, states.video, F.from_user.id.in_(ADMIN))
async def movie_add(message: Message, state: FSMContext):
    data = await state.get_data()
    movie_id = data.get('code')
    nomi = data.get('name')
    quality = data.get('quality')
    size = int(message.video.file_size / 1048576)
    views = 0

    text = f"""{nomi} | {quality}p
📀 Hajmi: {size} MB
🔡 (Kod: {movie_id})
"""

    movie = await bot.send_video(chat_id=-1002119835341, video=message.video.file_id, caption=text)

    message_id = movie.video.file_id

    add_movie_db(id=movie_id, name=nomi, quality=quality, size=size, views=views, message_id=message_id)

    await state.clear()

    await message.answer("Kino qo'shildi")

# ________________________________________________________________
