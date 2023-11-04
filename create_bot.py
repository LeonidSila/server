from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

# bot = Bot(token='6422120240:AAG43RB3FzmWoh0kHVDDcRs_llrRCeY0rw4') # НЕ РЕМ
bot = Bot(token='5971035628:AAFmlutJjpoujiONGx9_7RSwzFtN_KO6740') #РЕМ

# id_chat = '-1001966626424'
id_admin = 1443975003
id_chat = '-1001484566333' # Чат рабочей группы
dp = Dispatcher(bot, storage=storage)
