import time
import os
import tkinter as tk
from threading import Thread

def play_sound():
    sound_file = "reminder_sound.mp3"  # путь к звуковому файлу рядом с программой
    print(sound_file)
    if os.name == 'posix':  # Для Mac
        os.system(f'afplay {sound_file} &')
    elif os.name == 'nt':  # Для Windows
        os.system(f'start "" "{sound_file}"')

def check_list():
    with open('list.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        if line[0].isdigit() and int(line[0]) in [1, 2]:
            print(f" {line}")
            play_sound()
            time.sleep(1800)  # ждем 30 минут

def start_sound():
    global sound_thread
    sound_thread = Thread(target=check_list)
    sound_thread.start()

def stop_sound():
    if sound_thread.is_alive():
        sound_thread.join()

# Создание графического интерфейса
window = tk.Tk()
window.title("Звуковое напоминание")
window.geometry("300x100")

# Кнопка "Запустить"
start_button = tk.Button(window, text="Запустить", command=start_sound)
start_button.pack(pady=10)

# Кнопка "Остановить"
stop_button = tk.Button(window, text="Остановить", command=stop_sound)
stop_button.pack(pady=10)

# Запуск главного цикла графического интерфейса
window.mainloop()
