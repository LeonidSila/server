import sqlite3

from aiogram import types, Dispatcher
from create_bot import dp, bot, id_chat

from aiogram import types, Dispatcher
from create_bot import dp, id_chat, bot
import json, string
import time

conn = None
cursor = None
def creat_teble():
    global conn
    global cursor
    conn = sqlite3.connect('dbbot.sql')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id int AUTO_INCREMENT primary key, user_id int, user_name varchar(45), user_surname varchar(45), username varchar(45), quatity_day_message int default 0, quatity_week_message int default(0), quatity_yers_message int default(0), quatity_gey_day int default(0), quatity_gey int default(0), ban_list int default(0), rem_baks int default(0), opozdal int default(0), pidor_call int default(0), call_click int default(0))')
    conn.commit()







def register_handlers_db (dp : Dispatcher):
    dp.register_message_handler(creat_teble)