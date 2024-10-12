def get_cats_info(path):
    try:
        with open(path, encoding='utf-8') as file:
            cats_info = []
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cats_info.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Некоректний формат даних у рядку: {line.strip()}")
                    continue
            return cats_info
    except FileNotFoundError:
        print("Файл не знайдено, будь ласка, перевірте шлях до файлу.")
        return []
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
        return []


if __name__ == "__main__":

    # Приклад використання функції get_cats_info
    cats_info = get_cats_info("data_files/cats_file.txt")
    print(cats_info)
