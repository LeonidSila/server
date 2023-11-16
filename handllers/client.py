from aiogram import types, Dispatcher
from create_bot import dp, bot, id_chat
# from keyboards import client_kb
from db import db_bot 
import random
from docxtpl import DocxTemplate
from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram import FSMContext
from psh import psh_kek
import docx
import pathlib 
from pathlib import Path
import os
from huiver import huivet_kek
from dr_frend import key
from stikers import stikers_kek

# class Mydialog(StatesGroup):
#     otvet = State()
huivert_kto_oni = ''
komu_d = ''
orga = '' 
komu_name = ''
otkogo = '' 
otkogo_d = ''
otkogo_s = ''
d_1 = ''
m_1 = ''
g = ''

async def help_command(message : types.Message):
    us_id_1 = message.from_user.id
    await bot.send_message(us_id_1, text="Команды\n1) /pidor Рандомайзер\n2) /start /help - Пишет возмодности\n3) /PSH1 - Дает возмодность писать ПСЖ\n4) /pidorday - статистика пидоров в день\n5) /musikday - скидывает в чат музыку\n6) /huiver - Кто хуиверт\n7) /dr - Выбрать День рождения\n8) /stikers - Высылает стикер")
    
async def start_help(message : types.Message):
    us_name_1 = message.from_user.first_name
    await message.delete()
    await bot.send_message(chat_id = id_chat, text="ПОШЕЛ Нахуй - {0}".format(us_name_1))
    await bot.send_message(message.from_id, 'Так блять, это копия Викторя Альбинасовича. Данный бот следит за тем, как Вы работаете, сколько раз ТЫ НАХУЙ нажал разные кномпки да и в принципе активность. Если попали в бан, то либо вы Пидр, либо сбой уточните у администатора, как это так вышло, кек. Есть один момент, нельзя нахуй постонянно кликать и узнавать насколько ты ПИДР, ТЫ И ТАК ПИДР. НЕХУЙ ТЫКАТЬ. Перерыв будет 30 минут, иначе будет слать бывшие результаты.') 
    await message.delete()
    
async def db_imoprt(message : types.Message):
    us_id_1 = message.from_user.id
    us_name_1 = message.from_user.first_name
    us_sname_1 = message.from_user.last_name
    username_1 = message.from_user.username
    db_bot.cursor.execute('SELECT COUNT(*) FROM users WHERE user_id = ?', (us_id_1, ))
    us = db_bot.cursor.fetchone()
    us = us[0]
    if us == 0:
        db_bot.cursor.execute('INSERT INTO users (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (us_id_1, us_name_1, us_sname_1, username_1, ))
        db_bot.conn.commit()
        print('Добавил нового пользователя', us_id_1, us_name_1, us_sname_1, username_1)
    db_bot.conn.commit()
         
async def pidor_kek(message : types.Message):
    us_id_1 = message.from_user.id
    us_name_1 = message.from_user.first_name
    us_sname_1 = message.from_user.last_name
    username_1 = message.from_user.username
    db_bot.cursor.execute('SELECT COUNT(*) FROM users WHERE user_id = ?', (us_id_1, ))
    us = db_bot.cursor.fetchone()
    us = us[0]
    db_bot.conn.commit()
    if us == 0:
        await bot.send_message(chat_id = id_chat, text="А хули ты {0} не в Базе данных, напиши что-то".format(us_name_1))
    print(us_name_1, us_sname_1, username_1, "Проходит проверку на пидора")
    db_bot.cursor.execute('SELECT call_click FROM users WHERE user_id = ?', (us_id_1, ))
    us = db_bot.cursor.fetchone()
    us = us[0]
    db_bot.conn.commit()
    if us == 1:
        db_bot.cursor.execute('SELECT pidor_call FROM users WHERE user_id = ?', (us_id_1, ))
        us = db_bot.cursor.fetchone()
        us = us[0]
        db_bot.conn.commit()
        await bot.send_message(chat_id = id_chat, text="🏳️‍🌈 {1} на {0}% gay 🏳️‍🌈".format(int(us), us_name_1))
        # await bot.send_sticker(chat_id = id_chat, sticker= stikers_kek.list_stikers_group())
        await message.delete()
    else:
        db_bot.cursor.execute('SELECT pidor_call FROM users WHERE user_id = ?', (us_id_1, ))
        us = db_bot.cursor.fetchone()
        us = us[0]
        db_bot.conn.commit()
        pidor_random = random.randint(1, 100)
        await message.delete()
        await bot.send_message(chat_id = id_chat, text="🏳️‍🌈 {1} на {0}% gay 🏳️‍🌈".format(int(pidor_random), us_name_1))
        # await bot.send_sticker(chat_id = id_chat, sticker= stikers_kek.list_stikers_group())
        db_bot.cursor.execute('UPDATE users set pidor_call = ? where user_id = ?', (pidor_random, us_id_1, ))
        db_bot.conn.commit()
        db_bot.cursor.execute('UPDATE users set call_click = ? where user_id = ?', (1, us_id_1, ))
        db_bot.conn.commit()
        db_bot.cursor.execute('UPDATE users set quatity_gey_day = ? where user_id = ?', (pidor_random, us_id_1, ))
        db_bot.conn.commit()

async def pidor_kek_day(message : types.Message):
        await message.delete()
        db_bot.cursor.execute('SELECT quatity_gey_day, user_id, user_name, username FROM users')
        db_bot.conn.commit()
        us = db_bot.cursor.fetchall()
        sorted_tuple = tuple(sorted(us, reverse=True))
        sorted_tuple = sorted_tuple[0:3]
        await bot.send_message(chat_id = id_chat, text="Пидоры дня, к Вашему вниманию:\n\n{0} (--) {1}% \n🏳️‍🌈САМЫЙ, ГРЯЗЫЙ ПИДР ДНЯ🏳️‍🌈\n\n{2} (--) {3}% \n🏳️‍🌈ГРЯЗЫЙ ПИДР ДНЯ🏳️‍🌈\n\n{4} (--) {5}% \n🏳️ПИДР ДНЯ🏳️".format(sorted_tuple[0][2],  sorted_tuple[0][0], sorted_tuple[1][2], sorted_tuple[1][0], sorted_tuple[2][2], sorted_tuple[2][0]))
        # await bot.send_sticker(chat_id = id_chat, sticker= stikers_kek.list_stikers_group())
        
async def musik_kek(message : types.Message):
    await message.delete()
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
    
async def stiker_message(message : types.Message):
    await message.delete()
    # await bot.send_sticker(chat_id = id_chat, sticker= stikers_kek.list_stikers_group())
    
async def huivert(message : types.Message):
    user_id = message.from_user.id
    await bot.send_message(chat_id = user_id, text="Хуиверт КТО", reply_markup=huivet_kek.inline_button_huivert)
    await message.delete()
    
async def callback_huivert_leonid(callback: types.CallbackQuery):
    await bot.send_message(id_chat, text="Леонид ХУИВЕРТ")

async def callback_huivert_Alexei_b(callback: types.CallbackQuery):
    await bot.send_message(id_chat, text="Леха Браданосов ХУИВЕРТ")
    
async def callback_huivert_Viktor(callback: types.CallbackQuery):
    await bot.send_message(id_chat, text="ВИТЯ ХУИВЕРТ")

async def callback_huivert_Dmitri_b(callback: types.CallbackQuery):
    await bot.send_message(id_chat, text="Дмитрий Бучнев ХУИВЕРТ")
    
async def callback_huivert_Andrew(callback: types.CallbackQuery):
    await bot.send_message(id_chat, text="Андрей БРЕК ХУИВЕРТ хуй тебе а не премия")

async def callback_huivert_Prahur(callback: types.CallbackQuery):
    await bot.send_message(id_chat, text="Леха Попов ХУИВЕРТ")

async def callback_huivert_Evgeni(callback: types.CallbackQuery):
    await bot.send_message(id_chat, text="Женя ХУИВЕРТ")

async def callback_huivert_ilia(callback: types.CallbackQuery):
    await bot.send_message(id_chat, text="Илья ХУИВЕРТ")

async def callback_huivert_Ivan_B(callback: types.CallbackQuery):
    await bot.send_message(id_chat, text="Ваня Бучнев ХУИВЕРТ")

async def callback_huivert_Alexsei(callback: types.CallbackQuery):
    await bot.send_message(id_chat, text="Леха ХУИВЕРТ")

async def callback_huivert_Maxim(callback: types.CallbackQuery):
    await bot.send_message(id_chat, text="Петровский ХУИВЕРТ")

async def callback_huivert_Sergo(callback: types.CallbackQuery):
    await bot.send_message(id_chat, text="Сергей ХУИВЕРТ")

async def callback_huivert_di(callback: types.CallbackQuery):
    await bot.send_message(id_chat, text="DI ХУИВЕРТ")

    
async def callback_psg(message : types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    await bot.send_message(chat_id = id_chat, text="Этот чел {0} Пошел писать ПСЖ Пидр грязный, хуй ему и так людей нет. Меня не дергайте я не буду работать в этот промежуток".format(user_name))
    await bot.send_message(chat_id = user_id, text="Салам Чееел, выбери должность, кому ты пишешь", reply_markup=psh_kek.inline_button_list_directu)
    await message.delete()
    
async def callback_komu_orga(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global komu_d
    komu_d = 'Директору филиала'
    await bot.send_message(chat_id = us_id, text="А теперь выбери Огранизацию", reply_markup=psh_kek.inline_button_list_orga)
    
async def callback_komu_orga_2(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global komu_d
    komu_d = 'Заместителю директора филиала'
    await bot.send_message(chat_id = us_id, text="А теперь выбери Огранизацию", reply_markup=psh_kek.inline_button_list_orga)

async def callback_orga_name_1(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global orga
    orga = 'ФГУП ГРЧЦ в СЗФО'
    await bot.send_message(chat_id = us_id, text="Выбери Человека которому ты пишешь", reply_markup=psh_kek.inline_button_list_komu)
    
async def callback_orga_name_2(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global orga
    orga = 'ТЫ ПИДР'
    await bot.send_message(chat_id = us_id, text="Выбери Человека которому ты пишешь", reply_markup=psh_kek.inline_button_list_komu)

async def callback_orga_komu_1(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global komu_name
    komu_name  = 'А.Ю. Абрамову'
    await bot.send_message(chat_id = us_id, text="Кто ты воин?", reply_markup=psh_kek.inline_button_list_otkogo)

async def callback_orga_komu_2(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global komu_name
    komu_name  = 'В.М. Баранову'
    await bot.send_message(chat_id = us_id, text="Кто ты воин?", reply_markup=psh_kek.inline_button_list_otkogo)

async def callback_komu_name_1(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global otkogo
    otkogo = 'Силантьева Леонида Алексеевича'
    await bot.send_message(chat_id = us_id, text="Должность твоя, ты хуй!", reply_markup=psh_kek.inline_button_list_dolg)

async def callback_komu_name_2(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global otkogo
    otkogo = 'Бучнева Ивана Васильевича'
    await bot.send_message(chat_id = us_id, text="Должность твоя, ты хуй!", reply_markup=psh_kek.inline_button_list_dolg)

async def callback_komu_name_3(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global otkogo
    otkogo = 'Брека Андрея Александровича'
    await bot.send_message(chat_id = us_id, text="Должность твоя, ты хуй!", reply_markup=psh_kek.inline_button_list_dolg)

async def callback_komu_name_4(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global otkogo
    otkogo = 'Пастухова Дмитрия Вячеславовича'
    await bot.send_message(chat_id = us_id, text="Должность твоя, ты хуй!", reply_markup=psh_kek.inline_button_list_dolg)

async def callback_komu_name_5(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global otkogo
    otkogo = 'Гаврилина Виталия Михайловича'
    await bot.send_message(chat_id = us_id, text="Должность твоя, ты хуй!", reply_markup=psh_kek.inline_button_list_dolg)

async def callback_komu_name_6(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global otkogo_d
    otkogo_d = 'Салмыксова Андрея Николаевича'
    await bot.send_message(chat_id = us_id, text="Должность твоя, ты хуй!", reply_markup=psh_kek.inline_button_list_dolg)

async def callback_otkogo_dolg_1(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global otkogo_d
    otkogo_d = 'Инженер'
    await bot.send_message(chat_id = us_id, text="Твое подраздиление", reply_markup=psh_kek.inline_button_list_otkogo_s)

async def callback_otkogo_dolg_2(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global otkogo_d
    otkogo_d = 'Инженер 2-ой категории'
    await bot.send_message(chat_id = us_id, text="Твое подраздиление", reply_markup=psh_kek.inline_button_list_otkogo_s)    

async def callback_otkogo_dolg_3(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global otkogo_d
    otkogo_d = 'Ты пидр'
    await bot.send_message(chat_id = us_id, text="Твое подраздиление", reply_markup=psh_kek.inline_button_list_otkogo_s)    

async def callback_otkogo_dolg_4(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global otkogo_d
    otkogo_d = 'Инженер 1-ой категории'
    await bot.send_message(chat_id = us_id, text="Твое подраздиление", reply_markup=psh_kek.inline_button_list_otkogo_s)

async def callback_otkogo_s_date_1(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global otkogo_s
    otkogo_s = 'ОМРК УРК'
    await bot.send_message(chat_id = us_id, text="Выбери дату с кого дня ты уходишь", reply_markup=psh_kek.inline_button_list_d_1)    

async def callback_otkogo_s_date_2(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global otkogo_s
    otkogo_s = 'ГАМОГЕЙ'
    await bot.send_message(chat_id = us_id, text="Выбери дату с кого дня ты уходишь", reply_markup=psh_kek.inline_button_list_d_1)    

async def callback_otkogo_s_date_3(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global otkogo_s
    otkogo_s = 'НЕТ ЗП'
    await bot.send_message(chat_id = us_id, text="Выбери дату с кого дня ты уходишь", reply_markup=psh_kek.inline_button_list_d_1)

async def callback_date_mans_1(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '1'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_2(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '2'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_3(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '3'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)

async def callback_date_mans_4(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '4'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_5(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '5'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_6(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '6'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)

async def callback_date_mans_7(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '7'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_8(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '8'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_9(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '9'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)

async def callback_date_mans_10(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '10'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_11(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '11'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_12(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '12'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)

async def callback_date_mans_13(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '13'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_14(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '14'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_15(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '15'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)

async def callback_date_mans_16(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '16'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_17(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '17'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_18(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '18'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)

async def callback_date_mans_19(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '19'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_20(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '20'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_21(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '21'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)
    
async def callback_date_mans_22(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '22'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_23(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '23'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_24(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '24'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)
    
async def callback_date_mans_25(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '25'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_26(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '26'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_27(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '27'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)
    
async def callback_date_mans_28(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '28'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_29(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '29'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)    

async def callback_date_mans_30(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '30'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)

async def callback_date_mans_31(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global d_1
    d_1 = '31'
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=psh_kek.inline_button_list_manths_s)

async def callback_mans_yers_1(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global m_1
    m_1 = 'января'
    await bot.send_message(chat_id = us_id, text="Выбери год", reply_markup=psh_kek.inline_button_list_yers_s)

async def callback_mans_yers_2(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global m_1
    m_1 = 'февраля'
    await bot.send_message(chat_id = us_id, text="Выбери год", reply_markup=psh_kek.inline_button_list_yers_s)

async def callback_mans_yers_3(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global m_1
    m_1 = 'марта'
    await bot.send_message(chat_id = us_id, text="Выбери год", reply_markup=psh_kek.inline_button_list_yers_s)

async def callback_mans_yers_4(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global m_1
    m_1 = 'апреля'
    await bot.send_message(chat_id = us_id, text="Выбери год", reply_markup=psh_kek.inline_button_list_yers_s)

async def callback_mans_yers_5(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global m_1
    m_1 = 'мая'
    await bot.send_message(chat_id = us_id, text="Выбери год", reply_markup=psh_kek.inline_button_list_yers_s)

async def callback_mans_yers_6(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global m_1
    m_1 = 'июня'
    await bot.send_message(chat_id = us_id, text="Выбери год", reply_markup=psh_kek.inline_button_list_yers_s)
    
async def callback_mans_yers_7(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global m_1
    m_1 = 'июля'
    await bot.send_message(chat_id = us_id, text="Выбери год", reply_markup=psh_kek.inline_button_list_yers_s)

async def callback_mans_yers_8(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global m_1
    m_1 = 'августа'
    await bot.send_message(chat_id = us_id, text="Выбери год", reply_markup=psh_kek.inline_button_list_yers_s)
    
async def callback_mans_yers_9(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global m_1
    m_1 = 'сентября'
    await bot.send_message(chat_id = us_id, text="Выбери год", reply_markup=psh_kek.inline_button_list_yers_s)

async def callback_mans_yers_10(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global m_1
    m_1 = 'октября'
    await bot.send_message(chat_id = us_id, text="Выбери год", reply_markup=psh_kek.inline_button_list_yers_s)
    
async def callback_mans_yers_11(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global m_1
    m_1 = 'ноября'
    await bot.send_message(chat_id = us_id, text="Выбери год", reply_markup=psh_kek.inline_button_list_yers_s)

async def callback_mans_yers_12(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global m_1
    m_1 = 'декабря'
    await bot.send_message(chat_id = us_id, text="Выбери год", reply_markup=psh_kek.inline_button_list_yers_s)

async def callback_yers_all_1(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global g
    g = '2023'
    await bot.send_message(chat_id = us_id, text="Иди нахуй", reply_markup=psh_kek.inline_button_list_kek)

async def callback_yers_all_2(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global g
    g = '2024'
    await bot.send_message(chat_id = us_id, text="Иди нахуй", reply_markup=psh_kek.inline_button_list_kek)

async def callback_yers_all_3(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    global g
    g = '2025'
    await bot.send_message(chat_id = us_id, text="Иди нахуй", reply_markup=psh_kek.inline_button_list_kek)
    
async def vigruska_nahui(callback: types.CallbackQuery):
    await callback.answer(text="Вы пошли нахуй", show_alert=True)
    
async def dr_command(message : types.Message):
    await message.delete()
    us_id = message.from_user.id
    await bot.send_message(chat_id = us_id, text="Выбери день рождения, в прямом смысле день", reply_markup=key.inline_button_list_d_1)
  
async def vigruska(callback: types.CallbackQuery):
    global komu_d 
    global orga  
    global komu_name 
    global otkogo 
    global otkogo_d 
    global otkogo_s 
    global d_1 
    global m_1 
    global g 
    print(orga, type(orga))
    us_id = callback.from_user.id
    doc = DocxTemplate('hab.docx')
    # komu_d_all = {'komu_d_1' : str(komu_d)}
    # orga_all = {'orga_1' : str(orga)}
    # komu_name_all = {'komu_name_1' : str(komu_name)}
    # otkogo_all = {'otkogo_1' : str(otkogo)}
    # otkogo_d_all = {'otkogo_d_1' : str(otkogo_d)}
    # otkogo_s_all = {'otkogo_s_1' : str(otkogo_s)}
    # d_1_all = {'d_2' : str(d_1)}
    # m_1_all = {'m_2' : str(m_1)}
    # g_all = {'g_1' : str(g)}\
    # komu_d_all = {'komu' : komu_d}
    # orga_all = {'orga' : str(orga)}
    # komu_name_all = {'komus' : str(komu_name)}
    # otkogo_all = {'otkogofio' : str(otkogo)}
    # otkogo_d_all = {'otkogodolg' : str(otkogo_d)}
    # otkogo_s_all = {'otkogostruktura' : str(otkogo_s)}
    # d_1_all = {'d' : str(d_1)}
    # m_1_all = {'m' : str(m_1)}
    g_all = {'komu' : str(komu_d),
             'orga' : str(orga),
            'komus' : str(komu_name),
            'otkogofio' : str(otkogo),
            'otkogodolg' : str(otkogo_d),
            'otkogostruktura' : str(otkogo_s),
            'd' : str(d_1),
            'm' : str(m_1),
            'g' : str(g)}

# {'g' : str(g), 'komu' : str(komu_d), 'orga' : str(orga), 'komus' : str(komu_name), 
#              'otkogofio' : str(otkogo), 'otkogodolg' : str(otkogo_d), 'otkogostruktura' : str(otkogo_s),
#              'd' : str(d_1), 'm' : str(m_1)}

    # print(komu_d, komu_d_all, orga, orga_all, komu_name, komu_name_all, otkogo, otkogo_all, otkogo_s, otkogo_s_all)
    # context = {str(komu_d) : 'komu_d_1'}
    # doc.render(komu_d_all)
    # doc.render(orga_all)
    # doc.render(komu_name_all)
    # doc.render(otkogo_all)
    # doc.render(otkogo_d_all)
    # doc.render(otkogo_s_all)
    # doc.render(d_1_all)
    # doc.render(m_1_all)
    doc.render(g_all)
    doc.save('ПСЖ2.docx')
    file_path = "ПСЖ2.docx"
    input_file = types.InputFile(file_path)
    await bot.send_document(us_id, input_file)
    
 
 
    
def register_handlers_client (dp : Dispatcher):
    dp.register_message_handler(help_command, commands=['help_me'])
    dp.register_message_handler(pidor_kek, commands=['pidor'])
    dp.register_message_handler(start_help, commands=['start'])
    dp.register_message_handler(start_help, commands=['help'])
    dp.register_message_handler(callback_psg, commands=['PSH1'])
    dp.register_message_handler(pidor_kek_day, commands=['pidorday'])
    dp.register_message_handler(musik_kek, commands=['musikday'])
    dp.register_message_handler(huivert, commands=['huiver'])
    dp.register_message_handler(dr_command, commands=['dr'])
    dp.register_message_handler(stiker_message, commands=['stikers'])
    dp.register_callback_query_handler(callback_komu_orga, text='direkoru_1')
    dp.register_callback_query_handler(callback_komu_orga_2, text='direkoru_2')
    dp.register_callback_query_handler(callback_orga_name_1, text='orga_1')
    dp.register_callback_query_handler(callback_orga_name_2, text='orga_2')
    dp.register_callback_query_handler(callback_orga_komu_1, text='komu_name_1')
    dp.register_callback_query_handler(callback_orga_komu_2, text='komu_name_2')
    dp.register_callback_query_handler(callback_komu_name_1, text='otkogo_1')
    dp.register_callback_query_handler(callback_komu_name_2, text='otkogo_2')
    dp.register_callback_query_handler(callback_komu_name_3, text='otkogo_3')
    dp.register_callback_query_handler(callback_komu_name_4, text='otkogo_4')
    dp.register_callback_query_handler(callback_komu_name_5, text='otkogo_5')
    dp.register_callback_query_handler(callback_komu_name_6, text='otkogo_6')
    dp.register_callback_query_handler(callback_otkogo_dolg_1, text='dolg_1')
    dp.register_callback_query_handler(callback_otkogo_dolg_2, text='dolg_2')
    dp.register_callback_query_handler(callback_otkogo_dolg_3, text='dolg_3')
    dp.register_callback_query_handler(callback_otkogo_dolg_4, text='dolg_4')
    dp.register_callback_query_handler(callback_otkogo_s_date_1, text='otkogo_s_1')
    dp.register_callback_query_handler(callback_otkogo_s_date_2, text='otkogo_s_2')
    dp.register_callback_query_handler(callback_otkogo_s_date_3, text='otkogo_s_3')
    dp.register_callback_query_handler(callback_date_mans_1, text='d_1')
    dp.register_callback_query_handler(callback_date_mans_2, text='d_2')
    dp.register_callback_query_handler(callback_date_mans_3, text='d_3')
    dp.register_callback_query_handler(callback_date_mans_4, text='d_4')
    dp.register_callback_query_handler(callback_date_mans_5, text='d_5')
    dp.register_callback_query_handler(callback_date_mans_6, text='d_6')
    dp.register_callback_query_handler(callback_date_mans_7, text='d_7')
    dp.register_callback_query_handler(callback_date_mans_8, text='d_8')
    dp.register_callback_query_handler(callback_date_mans_9, text='d_9')
    dp.register_callback_query_handler(callback_date_mans_10, text='d_10')
    dp.register_callback_query_handler(callback_date_mans_11, text='d_11')
    dp.register_callback_query_handler(callback_date_mans_12, text='d_12')
    dp.register_callback_query_handler(callback_date_mans_13, text='d_13')
    dp.register_callback_query_handler(callback_date_mans_14, text='d_14')
    dp.register_callback_query_handler(callback_date_mans_15, text='d_15')
    dp.register_callback_query_handler(callback_date_mans_16, text='d_16')
    dp.register_callback_query_handler(callback_date_mans_17, text='d_17')
    dp.register_callback_query_handler(callback_date_mans_18, text='d_18')
    dp.register_callback_query_handler(callback_date_mans_19, text='d_19')
    dp.register_callback_query_handler(callback_date_mans_20, text='d_20')
    dp.register_callback_query_handler(callback_date_mans_21, text='d_21')
    dp.register_callback_query_handler(callback_date_mans_22, text='d_22')
    dp.register_callback_query_handler(callback_date_mans_23, text='d_23')
    dp.register_callback_query_handler(callback_date_mans_24, text='d_24')
    dp.register_callback_query_handler(callback_date_mans_25, text='d_25')
    dp.register_callback_query_handler(callback_date_mans_26, text='d_26')
    dp.register_callback_query_handler(callback_date_mans_27, text='d_27')
    dp.register_callback_query_handler(callback_date_mans_28, text='d_28')
    dp.register_callback_query_handler(callback_date_mans_29, text='d_29')
    dp.register_callback_query_handler(callback_date_mans_30, text='d_30')
    dp.register_callback_query_handler(callback_date_mans_31, text='d_31')
    dp.register_callback_query_handler(callback_mans_yers_1, text='m_1')
    dp.register_callback_query_handler(callback_mans_yers_2, text='m_2')
    dp.register_callback_query_handler(callback_mans_yers_3, text='m_3')
    dp.register_callback_query_handler(callback_mans_yers_4, text='m_4')
    dp.register_callback_query_handler(callback_mans_yers_5, text='m_5')
    dp.register_callback_query_handler(callback_mans_yers_6, text='m_6')
    dp.register_callback_query_handler(callback_mans_yers_7, text='m_7')
    dp.register_callback_query_handler(callback_mans_yers_8, text='m_8')
    dp.register_callback_query_handler(callback_mans_yers_9, text='m_9')
    dp.register_callback_query_handler(callback_mans_yers_10, text='m_10')
    dp.register_callback_query_handler(callback_mans_yers_11, text='m_11')
    dp.register_callback_query_handler(callback_mans_yers_12, text='m_12')
    dp.register_callback_query_handler(callback_yers_all_1, text='g_1')
    dp.register_callback_query_handler(callback_yers_all_2, text='g_2')
    dp.register_callback_query_handler(callback_yers_all_3, text='g_3')
    dp.register_callback_query_handler(vigruska_nahui, text='vigruzka_2')
    dp.register_callback_query_handler(vigruska, text='vigruzka_1')
    dp.register_callback_query_handler(callback_huivert_leonid, text='huiver_leonid')
    dp.register_callback_query_handler(callback_huivert_Alexei_b, text='huiver_alexei_b')
    dp.register_callback_query_handler(callback_huivert_Viktor, text='huiver_vity_K')
    dp.register_callback_query_handler(callback_huivert_Dmitri_b, text='huiver_dmitry_b')
    dp.register_callback_query_handler(callback_huivert_Andrew, text='huiver_andry_b')
    dp.register_callback_query_handler(callback_huivert_Prahur, text='huiver_alex_p')
    dp.register_callback_query_handler(callback_huivert_Evgeni, text='huiver_evgeni_k')
    dp.register_callback_query_handler(callback_huivert_ilia, text='huiver_ilia_k')
    dp.register_callback_query_handler(callback_huivert_Ivan_B, text='huiver_ivan_b')
    dp.register_callback_query_handler(callback_huivert_Alexsei, text='huiver_alexsei_k')
    dp.register_callback_query_handler(callback_huivert_Maxim, text='huiver_petrovski_m')
    dp.register_callback_query_handler(callback_huivert_Sergo, text='huiver_sergo_k')
    dp.register_callback_query_handler(callback_huivert_di, text='huiver_di_k')
    dp.register_message_handler(db_imoprt)
    


# def register_handlers_client (dp : Dispatcher):
#     dp.register_callback_query_handler(rem_baks_inline_butoon, text='rem_baks')
#     dp.register_message_handler(rem_baks_button, commands=['rem_baks'])
#     dp.register_message_handler(poidem_so_mnoi, commands=['вызывали?', 'Вызывали?', 'Вызывали', 'вызывали'])
#     dp.register_callback_query_handler(start_command_not_good, text='all_good_start_2')
#     dp.register_callback_query_handler(start_command_good, text='all_good_start_1')
#     dp.register_callback_query_handler(blagodarnost_callback, text='blagodarnost')
#     dp.register_callback_query_handler(callback_inline, text='pidor_random')
#     dp.register_message_handler(menu_fghz_command, commands=['menu'])
#     dp.register_message_handler(commands_start, commands=['start'])
#     dp.register_message_handler(help_command, commands=['help'])