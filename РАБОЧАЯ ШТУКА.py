import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import *
from string import punctuation
import pymorphy2

import os.path


def open_file():
    # открыть файл в формате .txt
    # используется диалоговое окно askopenfilename из модуля tkinter.filedialog,
    # чтобы отобразить диалоговое окно открытия файла и сохранить выбранный путь
    # к файлу в переменную filepath
    filepath = askopenfilename(
        filetypes=[('Текстовые файлы', '*.txt'), ('Все файлы', '*.*')]
    )
    if not filepath:
        return
    global save_name
    save_name = "morph_analyzer_" + os.path.basename(filepath)
    
    with open(filepath, 'r', encoding = 'utf-8') as input_file:
        text = input_file.read()
        words = text.split()
        clean_words = []
        for word in words:
            clean_words.append(word.strip(punctuation))

    
    with open(save_name, 'w', encoding = 'utf-8') as output_file:
        for i in clean_words:
            morph = pymorphy2.MorphAnalyzer()
            output_file.write(str(morph.parse(i)[0].word) + '\t' + (str(morph.parse(i)[0].tag)) + '\t' + (str(morph.parse(i)[0].normal_form)) + '\n')
    
    # txt_edit - текстовое поле
    # очищает текущее содержимое из текстового поля txt_edit,
    # используя метод .delete()
    txt_edit.delete('1.0', tk.END)

    
    with open(save_name, 'r', encoding = 'utf-8') as table:
        text_morph = table.read()
        # вставляем текст в текстовом поле txt_edit,
        # используя метод .insert()
        txt_edit.insert(tk.END, text_morph)
    window.title(f'morphAnalyzer - {filepath}')


def search_words():
    new_text = ''
    the_word = txt_search.get('1.0', END)

    with open(save_name, 'r', encoding = 'utf-8') as new_file:
        new = new_file.readlines()
        for line in new:
            if the_word in line:
                print(line)
                new_text += line

    txt_edit.delete('1.0', END)
    txt_edit.insert(tk.END, new_text)


#заголовок окна 
window = tk.Tk()
window.title('morphAnalyzer')

#установить минимальные размеры для окна и текстового поля
window.rowconfigure(0, minsize = 600, weight = 1)
window.columnconfigure(1, minsize = 600, weight = 1)

#создать поле для текста 
txt_edit = tk.Text(window, font = ('Helvetica', 17), cursor = 'sb_left_arrow', selectbackground = 'grey90')

#сделать кнопки и рамку для них (расположить их друг под другом)
fr_buttons = tk.Frame(window, relief = tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text = 'Открыть файл', command = open_file, font = ('Helvetica', 17))	
btn_search = tk.Button(fr_buttons, text = 'Поиск', command = search_words, font = ('Helvetica', 17))
txt_search = tk.Text(fr_buttons, cursor = 'top_left_corner', width = 10, height = 3, background = 'grey95', font = ('Helvetica', 17))

#расстояния в рамке (менеджер геометрии)
btn_open.grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 15)
txt_search.grid(row = 1, column = 0, sticky = 'ew', padx = 10, pady = 1)
btn_search.grid(row = 2, column = 0, sticky = 'nsew', padx = 10, pady = 0)
txt_search.mark_set("insert", "%d.%d" % (1,0))

#разместить кнопки и текстовое поле друг относительно друга 
fr_buttons.grid(row = 0, column = 0, sticky = 'ns')
txt_edit.grid(row = 0, column = 1, sticky = 'nsew')


window.mainloop()
