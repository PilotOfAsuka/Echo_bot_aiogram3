from aiogram.filters import Command
from aiogram.types import Message
from misc import dp


@dp.message(Command("start"))
async def start_handler(msg: Message):
    user_name = msg.from_user.username
    user_id = str(msg.from_user.id)
    # Отправляем приветственное сообщение
    await msg.answer(f"Привет {user_name}.\nБот ваш id: {user_id}")


@dp.message()
async def message_handler(msg: Message):
    user_name = msg.from_user.username
    msg_text = msg.text
    await msg.answer(f"Сообщение от {user_name}, {msg_text}")
