from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import os

bot = Bot(token=os.environ.get('BOT_TOKEN'), parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())
