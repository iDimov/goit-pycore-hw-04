import sys
import os
from pathlib import Path
try:
    from colorama import init, Fore
except ImportError:
    print("Бібліотека colorama не знайдена. Встановіть її за допомогою команди: pip install colorama")
    sys.exit(1)

# Ініціалізація colorama
init(autoreset=True)


def visualize_directory_structure(path):
    try:
        base_path = Path(path)
        if not base_path.exists() or not base_path.is_dir():
            print(Fore.RED + "Невірний шлях: директорія не існує або не є директорією.")
            return

        for root, dirs, files in os.walk(base_path):
            level = root.replace(str(base_path), '').count(os.sep)
            indent = ' ' * 4 * level
            print(Fore.BLUE + f"{indent}{os.path.basename(root)}/")
            sub_indent = ' ' * 4 * (level + 1)
            for d in dirs:
                print(Fore.BLUE + f"{sub_indent}{d}/")
            for f in files:
                print(Fore.GREEN + f"{sub_indent}{f}")
    except Exception as e:
        print(Fore.RED + f"Сталася помилка: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python directory_visualizer.py /шлях/до/директорії")
    else:
        visualize_directory_structure(sys.argv[1])
