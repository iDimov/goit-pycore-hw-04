def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                try:
                    _, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Некоректний формат даних у рядку: {line.strip()}")
                    continue

            if count == 0:
                return (0, 0)

            average = total / count
            return (total, average)
    except FileNotFoundError:
        print("Файл не знайдено, будь ласка, перевірте шлях до файлу.")
        return (0, 0)
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
        return (0, 0)


if __name__ == "__main__":
    # Приклад використання функції
    total, average = total_salary("./data_files/salary_file.txt")
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
