import datetime
from aiogram import Bot, types
from create_bot import id_chat
from db import db_bot
import random
import os 
import pathlib
from pathlib import Path


async def ytro(bot : Bot):  
    time_to_log = datetime.datetime.now()
    y = int(time_to_log.strftime('%Y'))
    m = int(time_to_log.strftime('%m'))
    d = int(time_to_log.strftime('%d'))
    ytro = datetime.datetime(year = y, month = m, day = d, hour = 8, minute = 30)
    ytro = ytro.strftime('%H:%M')
    # print(ytro)
    now_time = datetime.datetime.now()
    now_time = now_time.strftime('%H:%M')
    # print(now_time)
    if ytro == now_time:
        await bot.send_message(id_chat, 'Ну что у нас там?')
        print('Отправил утренне сообщение')

async def vesher(bot : Bot):
    time_to_log = datetime.datetime.now()
    y = int(time_to_log.strftime('%Y'))
    m = int(time_to_log.strftime('%m'))
    d = int(time_to_log.strftime('%d'))
    ytro = datetime.datetime(year = y, month = m, day = d, hour = 17, minute = 20)
    ytro = ytro.strftime('%H:%M')
    # print(ytro)
    now_time = datetime.datetime.now()
    now_time = now_time.strftime('%H:%M')
    # print(now_time)
    if ytro == now_time:
        await bot.send_message(id_chat, 'Георгичь пойдем! Че сидим?')
        print('Отправил Вечернее сообщение сообщение')

async def reset_pidor_click(bot : Bot):
    db_bot.cursor.execute('UPDATE users set call_click=0')
    db_bot.cursor.execute('UPDATE users set pidor_call=0')
    db_bot.conn.commit()
    print('Обнулил все нажание кнопки ПИДОР')

async def reset_pidor_stat(bot : Bot):
    time_to_log = datetime.datetime.now()
    y = int(time_to_log.strftime('%Y'))
    m = int(time_to_log.strftime('%m'))
    d = int(time_to_log.strftime('%d'))
    ytro = datetime.datetime(year = y, month = m, day = d, hour = 1, minute = 0)
    ytro = ytro.strftime('%H:%M')
    db_bot.cursor.execute('UPDATE users set quatity_gey_day=0')
    db_bot.conn.commit()
    print('Обнулил статистику ПИДОРА')

async def pidor_kek_day_time_1(bot : Bot):
    time_to_log = datetime.datetime.now()
    y = int(time_to_log.strftime('%Y'))
    m = int(time_to_log.strftime('%m'))
    d = int(time_to_log.strftime('%d'))
    ytro = datetime.datetime(year = y, month = m, day = d, hour = 8, minute = 30)
    ytro = ytro.strftime('%H:%M')
    ytro_1 = datetime.datetime(year = y, month = m, day = d, hour = 16, minute = 55)
    ytro_1 = ytro_1.strftime('%H:%M')
    # print(ytro)
    now_time = datetime.datetime.now()
    now_time = now_time.strftime('%H:%M')
    # print(now_time)
    if ytro == now_time or ytro_1 == now_time:
        db_bot.cursor.execute('SELECT quatity_gey_day, user_id, user_name, username FROM users')
        db_bot.conn.commit()
        us = db_bot.cursor.fetchall()
        sorted_tuple = tuple(sorted(us, reverse=True))
        sorted_tuple = sorted_tuple[0:3]
        await bot.send_message(chat_id = id_chat, text="Пидоры дня, к Вашему вниманию:\n\n{0} (--) {1}% \n🏳️‍🌈САМЫЙ, ГРЯЗЫЙ ПИДР ДНЯ🏳️‍🌈\n\n{2} (--) {3}% \n🏳️‍🌈ГРЯЗЫЙ ПИДР ДНЯ🏳️‍🌈\n\n{4} (--) {5}% \n🏳️ПИДР ДНЯ🏳️".format(sorted_tuple[0][2],  sorted_tuple[0][0], sorted_tuple[1][2], sorted_tuple[1][0], sorted_tuple[2][2], sorted_tuple[2][0]))

async def musik_time_kek(bot : Bot):
    time_to_log = datetime.datetime.now()
    y = int(time_to_log.strftime('%Y'))
    m = int(time_to_log.strftime('%m'))
    d = int(time_to_log.strftime('%d'))
    ytro = datetime.datetime(year = y, month = m, day = d, hour = 8, minute = 30)
    ytro = ytro.strftime('%H:%M')
    ytro_1 = datetime.datetime(year = y, month = m, day = d, hour = 16, minute = 55)
    ytro_1 = ytro_1.strftime('%H:%M')
    # print(ytro)
    now_time = datetime.datetime.now()
    now_time = now_time.strftime('%H:%M')
    # print(now_time)
    if ytro == now_time or ytro_1 == now_time:
        dir_path = pathlib.Path.cwd()
        path = Path(dir_path, 'musik')
        dirname = str(path)
        ext = ('.mp3')
        musik_229 = []
        for files in os.listdir(dirname):
            if files.endswith(ext):
                musik_229.append(files)
            else:
                continue
        musik_random = random.randint(1, len(musik_229))
        input_file = types.InputFile(('{0}\{1}'.format(dirname, musik_229[musik_random])))
        await bot.send_audio(id_chat, input_file)