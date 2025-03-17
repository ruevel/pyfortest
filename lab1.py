import tkinter as tk
from tkinter import messagebox

def determine_triangle_type(a, b, c):
    if a == b == c:
        return "равносторонний"
    elif a == b or a == c or b == c:
        return "равнобедренный"
    else:
        return "разносторонний"

def check_triangle():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())

        if a + b > c and a + c > b and b + c > a:
            triangle_type = determine_triangle_type(a, b, c)
            messagebox.showinfo("Результат", f"Полученный треугольник {triangle_type}")
        else:
            messagebox.showerror("Ошибка", "Треугольник с такими сторонами не существует")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа")


root = tk.Tk()
root.title("Определение типа треугольника")
root.configure(bg='blue')  

#ui
label_a = tk.Label(root, text="Сторона 1:", bg='lightblue', fg='black')
label_a.grid(row=0, column=0, padx=10, pady=10)

entry_a = tk.Entry(root, bg='lightblue', fg='black')
entry_a.grid(row=0, column=1, padx=10, pady=10)


label_b = tk.Label(root, text="Сторона 2:", bg='lightblue', fg='black')
label_b.grid(row=1, column=0, padx=10, pady=10)

entry_b = tk.Entry(root, bg='lightblue', fg='black')
entry_b.grid(row=1, column=1, padx=10, pady=10)


label_c = tk.Label(root, text="Сторона 3:", bg='lightblue', fg='black')
label_c.grid(row=2, column=0, padx=10, pady=10)

entry_c = tk.Entry(root, bg='lightblue', fg='black')
entry_c.grid(row=2, column=1, padx=10, pady=10)


check_button = tk.Button(root, text="Проверить", command=check_triangle, bg='green')
check_button.grid(row=3, column=0, columnspan=2)


root.mainloop()