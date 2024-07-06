# imports ________________________________________________________

# aiogram
from aiogram import Router, F
# aiogram filters
from aiogram.filters import CommandStart, Command
# aiogram fsm context
from aiogram.fsm.context import FSMContext
# aiogram types
from aiogram.types import Message
# db
from db import check_movie, get_movie, check_movies, get_movies

# settings _______________________________________________________

# router
router = Router()


# handlers _______________________________________________________

# users

@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer('Assalomu alaykum, agar siz menga kinoning kodini yuborsangiz men sizga uni topib beraman\nKinolarning ro\'yxatini ko\'rish: /list')

@router.message(Command('list'))
async def list(message:Message):
    if check_movies():
        data = get_movies()
        movies = ""
        for movie in data:
            movies+=f"Nomi: {movie[1]}\nKodi: {movie[0]}\n\n"
        await message.answer(movies)
    else:
        await message.answer("Hozirchalik kinolar ro'yxati bo'sh")

@router.message(F.text.isdigit() & ~F.text.startswith('0'))
async def send_movie(message: Message, state: FSMContext):
    if check_movie(movie_id=int(message.text)):
        movie = get_movie(movie_id=int(message.text))
        nomi = movie['name']
        quality = movie['quality']
        size = movie['size']
        movie_id = movie['id']

        text = f"""{nomi} | {quality}p
📀 Hajmi: {size} MB
🔡 (Kod: {movie_id})
"""
        await message.answer_video(video=movie['message_id'], caption=text)
    else:
        await message.answer(text="Bunaqa kodli film topilmadi")


# ________________________________________________________________
