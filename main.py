from string import punctuation
import pymorphy2
with open('what.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    words = text.split()
    clean_words = []
    for word in words:
        clean_words.append(word.strip(punctuation))
with open('table.txt', 'w', encoding='utf-8') as table:
    for i in clean_words:
        morph = pymorphy2.MorphAnalyzer()
        table.write(str(morph.parse(i)[0].word) + '\t' + (str(morph.parse(i)[0].tag)) + '\t' + (str(morph.parse(i)[0].normal_form)) + '\n')