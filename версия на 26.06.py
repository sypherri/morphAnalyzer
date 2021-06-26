import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

from string import punctuation
import pymorphy2

def open_file():
    # открыть файл в формате .txt
    #  диалоговое окно askopenfilename из модуля tkinter.filedialog нужно,
    # чтобы отобразить диалоговое окно открытия файла и сохранить выбранный путь
    # к файлу в переменную filepath
    filepath = askopenfilename(
        filetypes=[('Текстовые файлы', '*.txt'), ('Все файлы', '*.*')]
    )
    if not filepath:
        return

    with open(filepath, 'r', encoding = 'utf-8') as input_file:
        text = input_file.read()
        words = text.split()
        clean_words = []
        for word in words:
            clean_words.append(word.strip(punctuation))

    
    with open('morphAnalyzer.txt', 'w', encoding = 'utf-8') as output_file:
        for i in clean_words:
            morph = pymorphy2.MorphAnalyzer()
            output_file.write(str(morph.parse(i)[0].word) + '\t' + (str(morph.parse(i)[0].tag)) + '\t' + (str(morph.parse(i)[0].normal_form)) + '\n')

    # txt_edit - текстовое поле
    # далее очищаем текущее содержимое из текстового поля txt_edit,
    # используя метод .delete()
    txt_edit.delete('1.0', tk.END)
    
    with open('morphAnalyzer.txt', 'r', encoding = 'utf-8') as table:
        text_morph = table.read()
        # вставляем текст в текстовом поле txt_edit, используя метод .insert()
        txt_edit.insert(tk.END, text_morph)
    window.title(f'morphAnalyzer - {filepath}')

 
#заголовок окна 
window = tk.Tk()
window.title('morphAnalyzer')

#установить минимальные размеры для окна и текстового поля
window.rowconfigure(0, minsize = 800, weight = 1)
window.columnconfigure(1, minsize = 800, weight = 1)

#создать поле для текста 
txt_edit = tk.Text(window)

#сделать кнопки и рамку для них (расположить их друг под другом)
fr_buttons = tk.Frame(window, relief = tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text = 'Открыть файл', command = open_file, font = ('Helvetica', 17))
#btn_search = tk.Button(fr_buttons, text = 'Сохранить как', command = search_words, font = ('Helvetica', 17))

#расстояния в рамке (менеджер геометрии)
btn_open.grid(row = 0, column = 0, sticky = 'ew', padx = 10, pady = 10)
#btn_search.grid(row = 1, column = 0, sticky = 'ew', padx = 10)

#разместить кнопки и текстовое поле друг относительно друга 
fr_buttons.grid(row = 0, column = 0, sticky = 'ns')
txt_edit.grid(row = 0, column = 1, sticky = 'nsew')
 
window.mainloop()
