from tts import create_batch_tts 
import argparse

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



def main(dialog_path, output_folder, character_path):
    print("Этап 1 - Разбиение диалога на отдельные файлы")
    split_dialogues(dialog_path, output_folder)

    print("Этап 2 - Озвучка базовой моделью Silero")
    create_batch_tts(f"./{output_folder}/text", character_path)

    print("Этап 3 - Преобразование голоса через RVC")
    infer_files(f"./{output_folder}/tts", character_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('dialog_path', type=str, help='Путь к файлу с диалогами')
    parser.add_argument('output_folder', type=str, help='Путь к выходной папке')
    parser.add_argument('character_path', type=str, help='Путь к файлу с персонажами')

    args = parser.parse_args()
    main(args.dialog_path, args.output_folder, args.character_path)
