import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

# Создаем диспетчер для подключения обработчиков
dp = Dispatcher()
# Создаем клавиатуру с двумя кнопками в ряду
kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Основы Computer Science'), KeyboardButton(text='Основы Python')],
    [KeyboardButton(text='Telegram боты'), KeyboardButton(text='Фреймворк Django')],
    [KeyboardButton(text='Фреймворк Flask'), KeyboardButton(text='Фреймворк FastAPI')],
    [KeyboardButton(text='Python Developer Roadmap'), KeyboardButton(text='Наш GitHub')],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выбери интересующую тебя область')


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    '''
    Этот обработчик получает сообщения с помощью команды `/start`
    '''
    await message.answer(
        f'Привет, {message.from_user.full_name}!\n'
        'Го учить программирование и пайтон. Что тебя интересует?',
        reply_markup=kb
        )
    await message.delete()


@dp.message()
async def kb_message_handler(message: Message) -> None:
    '''
    Этот обработчик получает сообщения из клавиатуры
    '''
    # pattern matching (сопоставление шаблонов) работает начиная с версии Python 3.10
    match message.text:
        case 'Основы Computer Science':
            answer_message = 'Можешь начать с ознакомления с [данным плейлистом](https://www.youtube.com/playlist?list=PLt865Tpy2puXYHk2HhRfu1uXTrqz4deXs)'
        case 'Основы Python':
            answer_message = (
                'Можешь начать с ознакомления с [бесплатным курсом](https://stepik.org/course/58852/syllabus) от Stepik\n'
                'На платформе потребуется зарегистрироваться, но оно того стоит'
                )
        case 'Telegram боты':
            answer_message = 'Можешь начать с ознакомления с [данным плейлистом](https://youtube.com/playlist?list=PLYnH8mpFQ4am8cFYqn2KsPLb-HrhcYgtC&si=6Zgex5kd3-kGDWXw)'
        case 'Фреймворк Django':
            answer_message = (
                'Можешь начать с ознакомления с [данным плейлистом](https://www.youtube.com/playlist?list=PLNi5HdK6QEmWNqncVoUZtj1QDC2VV0wI6)\n'
                'Также многие рекомендуют книгу "Django 4 в примерах" Антонио Меле'
                )
        case 'Фреймворк Flask':
            answer_message = 'Можешь начать с ознакомления с [данным плейлистом](https://youtube.com/playlist?list=PLftd3YpHHMTNxBY7odYDaa4JYkNbceKJJ&si=42RezLkOUVBfk4jk)'
        case 'Фреймворк FastAPI':
            answer_message = 'Можешь начать с ознакомления с [данным плейлистом](https://youtube.com/playlist?list=PLftd3YpHHMTNxBY7odYDaa4JYkNbceKJJ&si=w3Jz94k5TD4_Fkow)'
        case 'Python Developer Roadmap':
            answer_message = (
                'Пошаговое руководство по тому, как стать разработчиком Python в 2024 году -\n'
                '[Python Developer Roadmap](https://extreme-poison-c6d.notion.site/Python-Roadmap-786bce62fb5f4db6b13cff63f76caae5?pvs=4)'
                )
        case 'Наш GitHub':
            answer_message = 'Ссылка на наш GitHub будет доступна позднее'
        case _:
            answer_message = 'Каво? Не понял'
    await message.reply(text=answer_message,
                        parse_mode='MarkdownV2')


async def main() -> None:
    '''
    Инициализирует экземпляр бота с использованием токена от @BotFather и запускает его
    '''
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
