import tkinter as tk
import secrets

def generate_key_part(initial_value, length, shift_direction='right'):
    key_part = ''
    for i in range(length):
        char_index = i % len(initial_value)
        current_char = initial_value[char_index]
        
        if current_char.isdigit():
            shift_amount = int(current_char)
            key_part += current_char
        else:
            key_part += current_char
        
        if shift_direction == 'right':
            current_char = chr((ord(current_char) + shift_amount - 48) % 36 + 48)
        else:
            current_char = chr((ord(current_char) - shift_amount - 48) % 36 + 48)
    
    return key_part

def generate_key():
    initial_value = input_entry.get()
    if not initial_value.isdigit() or len(initial_value) != 3:
        key_value.set("Ошибка: начальное значение должно быть трехзначным числом")
        return
    
    first_block = ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(5))
    second_block = generate_key_part(initial_value, 4, 'right')
    third_block = generate_key_part(initial_value, 3, 'left')
    fourth_block = generate_key_part(initial_value, 2, 'right')
    
    key = f"{first_block}-{second_block}-{third_block}-{fourth_block}"
    key_value.set(key)

# Создаем окно
root = tk.Tk()
root.title("Legend of Zelda Keygen")

# Добавляем фоновую картинку
background_image = tk.PhotoImage(file="zelda.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Добавляем поле для ввода первой части ключа
input_label = tk.Label(root, text="Введите первую часть ключа (трехзначное число):")
input_label.pack()

input_entry = tk.Entry(root)
input_entry.pack()

# Добавляем поле для отображения сгенерированного ключа
key_label = tk.Label(root, text="Сгенерированный ключ:")
key_label.pack()

key_value = tk.StringVar()
key_entry = tk.Entry(root, textvariable=key_value, state='readonly')
key_entry.pack()

# Добавляем кнопку для запуска генерации ключа
generate_button = tk.Button(root, text="Сгенерировать ключ", command=generate_key)
generate_button.pack()

# Отображаем окно
root.mainloop()
