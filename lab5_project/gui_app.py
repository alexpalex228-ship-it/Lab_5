"""GUI Приложение для Лабораторной работы № 5 (Вариант 2)."""

import tkinter as tk
from tkinter import ttk


def setup_task2_entry(parent: ttk.Notebook) -> ttk.Frame:
    """Задание 2 (Средняя): Окно с текстовым полем и кнопкой."""
    frame = ttk.Frame(parent)
    
    entry = ttk.Entry(frame, width=40)
    entry.pack(pady=20)
    
    label = ttk.Label(frame, text="Здесь появится ваш текст", font=("Arial", 12))
    label.pack(pady=10)
    
    def on_click():
        label.config(text=entry.get())
        
    btn = ttk.Button(frame, text="Вывести текст", command=on_click)
    btn.pack(pady=10)
    
    return frame


def setup_task4_listbox(parent: ttk.Notebook) -> ttk.Frame:
    """Задание 4 (Средняя): Список (Listbox) и выбор элемента."""
    frame = ttk.Frame(parent)
    
    label = ttk.Label(frame, text="Ничего не выбрано", font=("Arial", 12))
    label.pack(pady=10)
    
    listbox = tk.Listbox(frame, height=5, font=("Arial", 12))
    fruits = ["Яблоко", "Банан", "Апельсин", "Виноград", "Манго"]
    for item in fruits:
        listbox.insert(tk.END, item)
    listbox.pack(pady=10)
    
    def on_select(event):
        selected_indices = listbox.curselection()
        if selected_indices:
            item = listbox.get(selected_indices[0])
            label.config(text=f"Вы выбрали: {item}")
            
    listbox.bind('<<ListboxSelect>>', on_select)
    return frame


def setup_task2_high_draw(parent: ttk.Notebook) -> ttk.Frame:
    """Задание 2 (Повышенная): Рисование фигур мышью."""
    frame = ttk.Frame(parent)
    
    ttk.Label(frame, text="Рисуйте мышью (зажмите левую кнопку)").pack(pady=5)
    
    canvas = tk.Canvas(frame, bg="white", width=450, height=250)
    canvas.pack(pady=5)
    
    def paint(event):
        r = 3  # Радиус кисти
        canvas.create_oval(
            event.x - r, event.y - r, 
            event.x + r, event.y + r, 
            fill="black", outline="black"
        )
        
    canvas.bind("<B1-Motion>", paint)
    
    ttk.Button(frame, text="Очистить", command=lambda: canvas.delete("all")).pack()
    return frame


def setup_task6_high_converter(parent: ttk.Notebook) -> ttk.Frame:
    """Задание 6 (Повышенная): Программа «Конвертер валют»."""
    frame = ttk.Frame(parent)
    rates = {"USD": 1.0, "EUR": 0.92, "RUB": 92.5}
    
    ttk.Label(frame, text="Сумма:").pack(pady=5)
    amount_entry = ttk.Entry(frame)
    amount_entry.insert(0, "100")
    amount_entry.pack()
    
    ttk.Label(frame, text="Из валюты:").pack(pady=5)
    combo_from = ttk.Combobox(frame, values=list(rates.keys()), state="readonly")
    combo_from.set("USD")
    combo_from.pack()
    
    ttk.Label(frame, text="В валюту:").pack(pady=5)
    combo_to = ttk.Combobox(frame, values=list(rates.keys()), state="readonly")
    combo_to.set("RUB")
    combo_to.pack()
    
    result_label = ttk.Label(frame, text="Результат: ", font=("Arial", 12, "bold"))
    result_label.pack(pady=20)
    
    def convert():
        try:
            amt = float(amount_entry.get())
            rate_from = rates[combo_from.get()]
            rate_to = rates[combo_to.get()]
            result = (amt / rate_from) * rate_to
            result_label.config(text=f"Результат: {result:.2f} {combo_to.get()}")
        except ValueError:
            result_label.config(text="Ошибка: введите число!")
            
    ttk.Button(frame, text="Конвертировать", command=convert).pack()
    return frame


def main():
    root = tk.Tk()
    root.title("Лабораторная работа № 5")
    root.geometry("500x400")
    
    # Задание 7 (Средняя): Окно с меню (File -> Exit)
    menubar = tk.Menu(root)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=file_menu)
    root.config(menu=menubar)
    
    # Создаем вкладки
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both', padx=10, pady=10)
    
    # Добавляем задания на вкладки
    notebook.add(setup_task2_entry(notebook), text="Ввод текста")
    notebook.add(setup_task4_listbox(notebook), text="Список фруктов")
    notebook.add(setup_task2_high_draw(notebook), text="Рисование")
    notebook.add(setup_task6_high_converter(notebook), text="Конвертер")
    
    root.mainloop()


if __name__ == "__main__":
    main()