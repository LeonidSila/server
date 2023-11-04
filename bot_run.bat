@echo off

call %~dp0rem_sprot_bot_2\venv\Scriptsactivate

cd %~dp0rem_sprot_bot_2

python bot.py

pause