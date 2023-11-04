from aiogram import types, Dispatcher
from create_bot import dp, bot, id_chat
from dr_frend import key
from db import db_bot



async def callback_date_dr_1(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 1 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)    

async def callback_date_dr_2(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    
    db_bot.cursor.execute('UPDATE users set dr_day = 2 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)    

async def callback_date_dr_3(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 3 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)  

async def callback_date_dr_4(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 4 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)     

async def callback_date_dr_5(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 5 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)     

async def callback_date_dr_6(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 6 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)  

async def callback_date_dr_7(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 7 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)     

async def callback_date_dr_8(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 8 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)     

async def callback_date_dr_9(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 9 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)  

async def callback_date_dr_10(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 10 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)     

async def callback_date_dr_11(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 11 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)     

async def callback_date_dr_12(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 12 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)  

async def callback_date_dr_13(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 13 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)     

async def callback_date_dr_14(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 14 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)    

async def callback_date_dr_15(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 15 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)  

async def callback_date_dr_16(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 16 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)   

async def callback_date_dr_17(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 17 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)    

async def callback_date_dr_18(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 18 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)  

async def callback_date_dr_19(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 19 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)     

async def callback_date_dr_20(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 20 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)     

async def callback_date_dr_21(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 21 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)  
    
async def callback_date_dr_22(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 22 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)    

async def callback_date_dr_23(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 23 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)    

async def callback_date_dr_24(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 24 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)  
    
async def callback_date_dr_25(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 25 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)    

async def callback_date_dr_26(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 26 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)    

async def callback_date_dr_27(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 27 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)  
    
async def callback_date_dr_28(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 28 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)    

async def callback_date_dr_29(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 29 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)    

async def callback_date_dr_30(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 30 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr)  

async def callback_date_dr_31(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_day = 31 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Выбери месяц", reply_markup=key.inline_button_list_math_dr) 
    
     
    
async def callback_date_m_1(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_m = 1 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Ну все", reply_markup=key.inline_button_list_kek_hahui)  

async def callback_date_m_2(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_m = 2 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Ну все", reply_markup=key.inline_button_list_kek_hahui)  

async def callback_date_m_3(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_m = 3 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Ну все", reply_markup=key.inline_button_list_kek_hahui)  
    
async def callback_date_m_4(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_m = 4 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Ну все", reply_markup=key.inline_button_list_kek_hahui)  
    
async def callback_date_m_5(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_m = 5 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Ну все", reply_markup=key.inline_button_list_kek_hahui)  
    
async def callback_date_m_6(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_m = 6 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Ну все", reply_markup=key.inline_button_list_kek_hahui)  
    
async def callback_date_m_7(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_m = 7 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Ну все", reply_markup=key.inline_button_list_kek_hahui)  

async def callback_date_m_8(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_m = 8 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Ну все", reply_markup=key.inline_button_list_kek_hahui)  

async def callback_date_m_9(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_m = 9 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Ну все", reply_markup=key.inline_button_list_kek_hahui)  

async def callback_date_m_10(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_m = 10 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Ну все", reply_markup=key.inline_button_list_kek_hahui)  

async def callback_date_m_11(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_m = 11 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Ну все", reply_markup=key.inline_button_list_kek_hahui)  

async def callback_date_m_12(callback: types.CallbackQuery):
    us_id = callback.from_user.id
    db_bot.cursor.execute('UPDATE users set dr_m = 12 where user_id = ?', ( us_id, ))
    db_bot.conn.commit()
    await bot.send_message(chat_id = us_id, text="Ну все", reply_markup=key.inline_button_list_kek_hahui)  
    
async def dr_nahui(callback: types.CallbackQuery):
    await callback.answer(text="Вы пошли нахуй", show_alert=True)


  



def register_handlers_client (dp : Dispatcher):
    dp.register_callback_query_handler(callback_date_dr_1, text='dr_1')
    dp.register_callback_query_handler(callback_date_dr_2, text='dr_2')
    dp.register_callback_query_handler(callback_date_dr_3, text='dr_3')
    dp.register_callback_query_handler(callback_date_dr_4, text='dr_4')
    dp.register_callback_query_handler(callback_date_dr_5, text='dr_5')
    dp.register_callback_query_handler(callback_date_dr_6, text='dr_6')
    dp.register_callback_query_handler(callback_date_dr_7, text='dr_7')
    dp.register_callback_query_handler(callback_date_dr_8, text='dr_8')
    dp.register_callback_query_handler(callback_date_dr_9, text='dr_9')
    dp.register_callback_query_handler(callback_date_dr_10, text='dr_10')
    dp.register_callback_query_handler(callback_date_dr_11, text='dr_11')
    dp.register_callback_query_handler(callback_date_dr_12, text='dr_12')
    dp.register_callback_query_handler(callback_date_dr_13, text='dr_13')
    dp.register_callback_query_handler(callback_date_dr_14, text='dr_14')
    dp.register_callback_query_handler(callback_date_dr_15, text='dr_15')
    dp.register_callback_query_handler(callback_date_dr_16, text='dr_16')
    dp.register_callback_query_handler(callback_date_dr_17, text='dr_17')
    dp.register_callback_query_handler(callback_date_dr_18, text='dr_18')
    dp.register_callback_query_handler(callback_date_dr_19, text='dr_19')
    dp.register_callback_query_handler(callback_date_dr_20, text='dr_20')
    dp.register_callback_query_handler(callback_date_dr_21, text='dr_21')
    dp.register_callback_query_handler(callback_date_dr_22, text='dr_22')
    dp.register_callback_query_handler(callback_date_dr_23, text='dr_23')
    dp.register_callback_query_handler(callback_date_dr_24, text='dr_24')
    dp.register_callback_query_handler(callback_date_dr_25, text='dr_25')
    dp.register_callback_query_handler(callback_date_dr_26, text='dr_26')
    dp.register_callback_query_handler(callback_date_dr_27, text='dr_27')
    dp.register_callback_query_handler(callback_date_dr_28, text='dr_28')
    dp.register_callback_query_handler(callback_date_dr_29, text='dr_29')
    dp.register_callback_query_handler(callback_date_dr_30, text='dr_30')
    dp.register_callback_query_handler(callback_date_dr_31, text='dr_31')
    
    dp.register_callback_query_handler(callback_date_m_1, text='m_dr_1')
    dp.register_callback_query_handler(callback_date_m_2, text='m_dr_2')
    dp.register_callback_query_handler(callback_date_m_3, text='m_dr_3')
    dp.register_callback_query_handler(callback_date_m_4, text='m_dr_4')
    dp.register_callback_query_handler(callback_date_m_5, text='m_dr_5')
    dp.register_callback_query_handler(callback_date_m_6, text='m_dr_6')
    dp.register_callback_query_handler(callback_date_m_7, text='m_dr_7')
    dp.register_callback_query_handler(callback_date_m_8, text='m_dr_8')
    dp.register_callback_query_handler(callback_date_m_9, text='m_dr_9')
    dp.register_callback_query_handler(callback_date_m_10, text='m_dr_10')
    dp.register_callback_query_handler(callback_date_m_11, text='m_dr_11')
    dp.register_callback_query_handler(callback_date_m_12, text='m_dr_12')
    
    dp.register_callback_query_handler(dr_nahui, text='hahui_1')
    
    
    
