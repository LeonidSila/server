from aiogram import executor
from create_bot import dp
from handllers import client
from db import db_bot
from create_bot import bot as bt
from time_clik import time_lol
from dr_frend import dr_frend_kek

db_bot.creat_teble()
from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from time_work import time_lol
# from datetime import datetime, timedelta

scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

scheduler.add_job(time_lol.ytro, trigger='interval', seconds = 60, kwargs={'bot': bt})
scheduler.add_job(time_lol.vesher, trigger='interval', seconds = 60, kwargs={'bot': bt})
scheduler.add_job(time_lol.reset_pidor_click, trigger='interval', seconds = 400, kwargs={'bot': bt})
scheduler.add_job(time_lol.pidor_kek_day_time_1, trigger='interval', seconds = 60, kwargs={'bot': bt})
scheduler.add_job(time_lol.musik_time_kek, trigger='interval', seconds = 60, kwargs={'bot': bt})
scheduler.add_job(time_lol.reset_pidor_stat, trigger='interval', seconds = 172800, kwargs={'bot': bt})
# scheduler.add_job(time_lol.reset_opozdal_chethick_rem, trigger='interval', seconds = 86400, kwargs={'bot': bt})
# scheduler.add_job(time_lol.reset_call_click_day, trigger='interval' , seconds = 10800, kwargs={'bot': bt})
# scheduler.add_job(time_lol.reset_call_click_week, trigger='interval' , seconds = 82800, kwargs={'bot': bt})   

scheduler.start()

# admin.register_handlers_admin(dp)
dr_frend_kek.register_handlers_client(dp)
client.register_handlers_client(dp)
db_bot.register_handlers_db(dp)

executor.start_polling(dp, skip_updates=True)