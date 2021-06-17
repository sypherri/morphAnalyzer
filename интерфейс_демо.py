import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    #открыть файл в формате .txt
    filepath = askopenfilename(
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )

    if not filepath:
        return

    txt_edit.delete("1.0", tk.END)

    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)


 
def save_file():
    #сохранить файл как новый в формате .txt
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
    )

    if not filepath:
        return

    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
 
#заголовок окна 
window = tk.Tk()
window.title("Прога_Прога")

#установить минимальные размеры для окна и текстового поля
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

#создать поле для текста 
txt_edit = tk.Text(window)

#сделать кнопки и рамку для них (расположить их друг под другом)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Открыть файл", command=open_file, font=('Helvetica', 17))
btn_save = tk.Button(fr_buttons, text="Сохранить как", command=save_file, font=('Helvetica', 17))

#расстояния в рамке (менеджер геометрии)
btn_open.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
btn_save.grid(row=1, column=0, sticky="ew", padx=10)

#разместить кнопки и текстовое поле друг относительно друга 
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

 
window.mainloop()
