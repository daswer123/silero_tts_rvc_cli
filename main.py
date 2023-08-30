from tts import create_batch_tts 

import os
import re
from infer_rvc import infer_files
from tts import create_batch_tts

def split_dialogues(input_file, output_directory):
    # Создаем папку, если она еще не существует
    output_directory = os.path.join(output_directory,"text")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(input_file, 'r', encoding='utf-8') as file:
        data = file.read()

    dialogues = re.split(r'(\w+:)', data)

    for i in range(1, len(dialogues), 2):
        speaker = dialogues[i].strip(': ')
        text = dialogues[i+1].strip()

        filename = f'{i//2+1}_{speaker}.txt'
        filename = filename.replace(" ", "_")  # Замена пробелов на подчеркивания в имени файла
        with open(os.path.join(output_directory, filename), 'w', encoding='utf-8') as out_file:
            out_file.write(f'{speaker}: {text}\n')

print("Этап 1 - разбиение на отдельные файлы")
split_dialogues("test.txt","dialog1")

print("Этап 2 - озвучка базовой моделью Silero")
create_batch_tts("./dialog1/text","character.json")

print("Этап 3 - преобразование голоса через RVC")
infer_files("./dialog1/tts","character.json")