from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from handllers import client as c

button_huiver_leonid = InlineKeyboardButton(text='Леонид', callback_data='huiver_leonid')
button_huiver_Alexei_b = InlineKeyboardButton(text='Алексей Бараданосов', callback_data='huiver_alexei_b')
button_huiver_Viktor = InlineKeyboardButton(text='Витя Киприянов', callback_data='huiver_vity_K')
button_huiver_Dmitri_b = InlineKeyboardButton(text='Дмитрий Бучнев', callback_data='huiver_dmitry_b')
button_huiver_Andrew = InlineKeyboardButton(text='Андрей Брек', callback_data='huiver_andry_b')
button_huiver_Prahur = InlineKeyboardButton(text='Алексей Попов', callback_data='huiver_alex_p')
button_huiver_Evgeni = InlineKeyboardButton(text='Какой то Евгенией', callback_data='huiver_evgeni_k')
button_huiver_ilia = InlineKeyboardButton(text='Какой-то Илья', callback_data='huiver_ilia_k')
button_huiver_Ivan_B= InlineKeyboardButton(text='Иван Бучнев', callback_data='huiver_ivan_b')
button_huiver_Alexsei = InlineKeyboardButton(text='Какой-то Алексей', callback_data='huiver_alexsei_k')
button_huiver_Maxim = InlineKeyboardButton(text='Петровский Максим', callback_data='huiver_petrovski_m')
button_huiver_Sergo = InlineKeyboardButton(text='Какой-то Сергей', callback_data='huiver_sergo_k')
button_huiver_di = InlineKeyboardButton(text='Какой-то di', callback_data='huiver_di_k')


inline_button_huivert = InlineKeyboardMarkup().add(button_huiver_leonid, 
                                                        button_huiver_Alexei_b, 
                                                        button_huiver_Viktor,
                                                        button_huiver_Dmitri_b,
                                                        button_huiver_Andrew,
                                                        button_huiver_Prahur,
                                                        button_huiver_Evgeni,
                                                        button_huiver_ilia,
                                                        button_huiver_Ivan_B,
                                                        button_huiver_Alexsei,
                                                        button_huiver_Maxim,
                                                        button_huiver_Sergo,
                                                        button_huiver_di)


