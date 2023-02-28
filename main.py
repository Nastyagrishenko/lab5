# С клавиатуры вводятся поочередно N слов. Напишите программу, которая соединяет эти слова в одну длинную строку.

stroka=[]
m=3
for i in range(m):
    stroka.append(imput())
    word = ''. join(stroka)



print()