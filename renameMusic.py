import os
import random

def process_music_files(folder_path):
    # Получаем список всех файлов в папке
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Убираем первые три символа из названия файла и имени автора
    processed_files = []
    for file in files:
        if len(file) > 3:
            new_name = file[3:]
            processed_files.append(new_name)

    # Перемешиваем треки
    random.shuffle(processed_files)

    # Добавляем номера в зависимости от порядка
    renamed_files = []
    for i, file in enumerate(processed_files):
        number = str(i + 1).zfill(3)  # Генерируем номер с ведущими нулями
        new_file_name = f"{number}_{file}"
        renamed_files.append(new_file_name)

    # Применяем изменения к файлам: временное переименование для исключения конфликтов
    temp_files = []
    for old_name in files:
        temp_name = f"temp_{old_name}"
        os.rename(os.path.join(folder_path, old_name), os.path.join(folder_path, temp_name))
        temp_files.append(temp_name)

    # Финальное переименование с учетом нового порядка
    for temp_name, new_name in zip(temp_files, renamed_files):
        temp_path = os.path.join(folder_path, temp_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(temp_path, new_path)

    print("Треки успешно обработаны и переименованы!")

# Пример использования:
# Укажите путь к папке с музыкальными файлами
music_folder = "E:\CD1"
process_music_files(music_folder)
