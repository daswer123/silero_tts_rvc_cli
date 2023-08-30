@echo off

:: Измените пути в этих переменных под свои
set "DIALOG_PATH=test.txt"
set "OUTPUT_FOLDER=dialog1"
set "CHARACTER_PATH=character.json"


call venv/scripts/activate
python main.py "%DIALOG_PATH%" "%OUTPUT_FOLDER%" "%CHARACTER_PATH%"