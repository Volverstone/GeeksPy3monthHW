from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

admin = [2031978710,]
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
storege = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storege)