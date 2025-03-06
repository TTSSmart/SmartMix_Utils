from pathlib import Path

# Путь к папке с логами
errors_path = "C:/Users/Главный пользователь/Desktop/Новая папка/Logs/2"

# Функция для поиска строк с ошибками в файлах
def find_error_lines(file_path):
    error_lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Ищем строки, содержащие "[ERROR]"
            if "[ERROR]" in line:
                error_lines.append(line.strip())  # Удаляем лишние пробелы и переносы строк
    return error_lines

# Получение списка всех .txt файлов в папке
p = Path(errors_path)
txt_files = p.rglob("*.txt")

# Словарь для хранения ошибок по файлам
error_dict = {}

# Обработка каждого файла
for txt_file in txt_files:
    if txt_file.is_file():  # Проверяем, что это файл
        print(f"Обработка файла: {txt_file}")
        errors = find_error_lines(txt_file)
        if errors:
            error_dict[txt_file.name] = errors  # Сохраняем ошибки по имени файла

# Вывод результатов
if error_dict:
    print("\nНайденные ошибки:")

    # Открываем файл для записи ошибок
    with open('full_errors.txt', 'w', encoding="utf-8") as output_file:
        for file_name, errors in error_dict.items():
            print(f"\nФайл: {file_name}")
            output_file.write(f"=== Файл: {file_name} ===\n")  # Разделитель для файла

            for error in errors:
                print(error)
                output_file.write(f"{error}\n")  # Записываем ошибку в файл

            output_file.write("\n")  # Добавляем пустую строку между файлами
else:
    print("Ошибки не найдены.")