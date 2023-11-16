import random


# list_stikers = {0: 'CAACAgIAAxkBAAEBpZVlPUaXde8RHm_dcIyzfmfu5AFQUAACVQADuzjpERLv2C2Z5WaTMAQ',
#                     1: 'CAACAgIAAxkBAAEBpZdlPUacwfMlYxEtz58ho7ww4fZTxQACVAADuzjpEYixx3J5IRCxMAQ',
#                     2: 'CAACAgIAAxkBAAEBpZllPUaemYsCWELOG-shyvtEQtpK4QACPgADuzjpEYhkEGmcp_PEMAQ',
#                     3: 'CAACAgIAAxkBAAEBpZtlPUam0t-jkWvYtOaqwsjHW89uxAACUQADuzjpET2aLxYVcPPGMAQ',
#                     4: 'CAACAgIAAxkBAAEBpZ1lPUatj0msfMfcsFOFo8SZg5t6JwACGAADuzjpEev6xwzwl5byMAQ',
#                     5: 'CAACAgIAAxkBAAEBpZ9lPUax2jWHIWDaVx5otKCTwQwJKwACBgADuzjpEU7-wWWpyUAGMAQ',
#                     6: 'CAACAgIAAxkBAAEBpaFlPUa0drZa5ytoFB8N69mo9K7ZJwACAQADuzjpEQMJtJ1DvxBZMAQ',
#                     7: 'CAACAgIAAxkBAAEBpellPUb4chfH8WJll0pxUVrQE2Gk0QACMwEAAlwMchu3rzh-YLb1bDAE',
#                     8: 'CAACAgIAAxkBAAEBpetlPUb6wr3RcBzS1CxPB6cpb2Zu-wACOQEAAlwMchv8xvc9OOCDATAE', 
#                     9: 'CAACAgIAAxkBAAEBpe9lPUb9a9TiGAlMhD2gIDhaf3pcxgACNgEAAlwMcht-ZJylPsmgiDAE', 
#                     10: 'CAACAgIAAxkBAAEBpfNlPUcEqdh0uqj_xMkoS0x4sZ46FwACPQEAAlwMchvzFOiE82xEmzAE', 
#                     11: 'CAACAgIAAxkBAAEBpfVlPUcHJCKM4izGsCbtZR-PXiZClwACHxwAAgOf6UvFNCJkZYfKQDAE',
#                     12: 'CAACAgIAAxkBAAEBpf1lPUcTtS34rc5reU7f0F4P3pHGHwACFxUAAspwgEgQIknBzTeVSjAE',
#                     13: 'CAACAgIAAxkBAAEKpWRlQNLeDX8S_GvMsTSdPv022tfMDQACCCMAAvbtmUlF5zb-PN1B-jME',
#                     14: 'CAACAgIAAxkBAAEKpWZlQNLiv616ixQQxBwYovom3yEQAwACGzoAAkwgoUlPd75AUEFeFzME',
#                     15: 'CAACAgIAAxkBAAEKpWhlQNLsaz5bOcQpUzXn4R9O6AGzhwACqz0AAorHuEjdJ6DYGHpjozME',
#                     16: 'CAACAgIAAxkBAAEKpWplQNLvnL5uX96j-Te86JhETMtBNwACch0AAmvf-Uqjz605p60YSTME', 
#                     17: 'CAACAgIAAxkBAAEKpWxlQNL1bLw5BGhljc8ClwxNZcl_MQAC2zMAAkPYUUoLKMAMcBWuJDME', 
#                     18: 'CAACAgIAAxkBAAEKpW5lQNL36iaCZWWa4QxHDVfudZQ_nQACChcAAjDB6UmMiYQVwNCN2zME',
#                     19: 'CAACAgIAAxkBAAEKpXBlQNL6kVHDKrKI4_eC--13_9ANhwACVh8AAuPP8Uku_dgNeFcqszME', 
#                     20: 'CAACAgIAAxkBAAEKpXJlQNMBGv3jRXaN0NaqsKitCIJdJgACfRoAAiTGMUod5JQZJBNXjjME', 
#                     21: 'CAACAgIAAxkBAAEKpXRlQNMKvLaBrv_XCE7m0qFp_TNlRwACTQADI0MjBOI8uXDt5018MwQ', 
#                     22: 'CAACAgIAAxkBAAEKpXZlQNMuhXNbG-dO01bYTvR7d68hLQACfQADhbMkCRjhmwTL8akxMwQ',
#                     23: 'CAACAgIAAxkBAAEKpXhlQNOxAoLOb4jr_LYnpzRJir-IsAACdwkAAu24mUjk0O4KiAd1szME',
#                     24: 'CAACAgIAAxkBAAEKpXplQNSjJ9yv99KsolwCQBF7tpaJEAACzAADWuOKF7M_K2-fBFWMMwQ',
#                     25: 'CAACAgIAAxkBAAEKpXxlQNSoqiUtXQIEZhgKp02-0j8ipgAC3QADWuOKFwVtiLMOZ0pFMwQ',
#                     26: 'CAACAgIAAxkBAAEKpX5lQNSrJIq6toXhjnPikOMYk8-IjwAC4gADWuOKF9AZseRWe1REMwQ',
#                     27: 'CAACAgIAAxkBAAEKpYBlQNSuf8suuFGu2THl53q7Wvy_nwAC3wADWuOKF2G9ts8PtHxJMwQ',
#                     28: 'CAACAgIAAxkBAAEKpYJlQNSysDf5GQi9EJkasvGvB73JVwAC7QADWuOKFwZhXpyPsrMmMwQ',
#                     29: 'CAACAgIAAxkBAAEKpYRlQNS3CnGdrM00bkVPsaes7bncEAACbQEAAlrjihd0jFsNbtTmnDME',
#                     30: 'CAACAgIAAxkBAAEKpYZlQNTAU02p_R-gxbU_P0ycAAGy0LsAAj4CAAJa44oX3Cmg_3OtHn4zBA',
#                     31: 'CAACAgIAAxkBAAEKpYhlQNTLG461x6kZvrYHEwABeiVveFIAAh0EAAJa44oXaJW1lB4mzXczBA',
#                     32: 'CAACAgIAAxkBAAEKpZNlQNbFcrG6xKYSSawPRRRjaN20KwACzw4AAv4vsEuuJ4raX-d5oTME',
#                     33: 'CAACAgIAAxkBAAEKpZVlQNbJmcdJyJjPE5AJPygICe_E1QACEw0AAvlZwEvM6in1HYvV6jME',
#                     34: 'CAACAgIAAxkBAAEKpZdlQNbbK9NETIoczUfj1vJUpvBDRAAC0xQAAp4EwEt8zuy8m-EnkzME',
#                     35: 'CAACAgIAAxkBAAEKpZllQNbk8rXiMrC3qRXPSzbl-s7G5AAC8iMAAsZcyUtLyBoYijDvTTME',
#                     36: 'CAACAgIAAxkBAAEKpZtlQNbs7JOhx8vJSTB5Vst42db-EgACGBQAAktbCUhi5aji9aj16TME',
#                     37: 'CAACAgIAAxkBAAEKpZ1lQNbvLk2gX2HSPRhl4efurawBTgACfBYAAg7OCUj_7CUTdeHh6zME',
#                     38: 'CAACAgIAAxkBAAEKpZ9lQNbzm6UPwtvUa9EAAbADFjDJBOoAApsTAAKjZhBIhn7zOLY51FQzBA',
#                     39: 'CAACAgIAAxkBAAEKpaFlQNb7DswqDM6wSPpeZ2MMGG5wkQACRhUAAp2FCUgDX1FwOkstfjME',
#                     40: 'CAACAgIAAxkBAAEKpaNlQNcDD0ECDvg2CGwh6kMzSwx3xQACfBUAAlFEEEi5K5_rLG8x3jME',
#                     41: 'CAACAgIAAxkBAAEKpaVlQNcMdXkhS8k_Yji7hj6Gpwx3yQACsRYAAgvVCEhTQocFGegLhzME',
#                     42: 'CAACAgIAAxkBAAEKpadlQNcT19CPeb4Vhxl8U31XAAGkF7cAAq0TAAILAghIxq4NujDxa78zBA',
#                     43: 'CAACAgIAAxkBAAEKpallQNcWhpGUuPPZsLizazWqbPlOzAAChxgAAtd9CUh_3VSsNHRo5jME',
#                     44: 'CAACAgIAAxkBAAEKpatlQNcYxzzFY1RI8FkAAQFkk66KbmgAAroUAAJ7sxBIIJ-c2wEZS0wzBA',
#                     45: 'CAACAgIAAxkBAAEKpa1lQNcjeNnDDHnd5-LXKV9ycQxMTQACTxQAAlhrsUhO1FrIbuv27zME',
#                     46: 'CAACAgIAAxkBAAEKpa9lQNcm5OrW6F6MzY9HxlnSQHqj4AACWxMAAt9osUiI7mTOK4rT2zME',
#                     47: 'CAACAgIAAxkBAAEKpbFlQNcs9rVbOubyrf3cyZkNawEUfgACYAADKcn5BgqmFb1yGuNYMwQ',
#                     48: 'CAACAgIAAxkBAAEKpbNlQNczidTbM4w7HBZKTh8Z7py57AACjAADKcn5Br0RL_saFn3vMwQ',
#                     49: 'CAACAgIAAxkBAAEKpbVlQNc4DF_HvwfyWwoICLipsNxotgACvAADKcn5Br8p4suuJSmVMwQ',
#                     50: 'CAACAgIAAxkBAAEKpbdlQNc7EhkqIVIwWZ0YyxZzMvAHVQACJAIAAinJ-Qbsu_q10AzqLTME'
                    
                    
#                     }
    
# def list_stikers_group():
#     len_stikers = len(list_stikers)
#     random_list_stikers = random.randrange(len_stikers-1)
#     return list_stikers[random_list_stikers]
    

