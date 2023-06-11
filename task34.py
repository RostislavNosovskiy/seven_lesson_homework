# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко
# он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое
# . Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в 
# порядке
# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  
vinnilyric = input('Введите стихотворение Винни-Пуха')
vinnilyricinlist = vinnilyric.split()
print(vinnilyricinlist)
def countvowelinwotd (word):
    countofvowel =0
    for i in range (len(word)):
        if word[i]=='а' or word[i] == 'и' or word[i] == 'о' or word[i] == 'у' or word[i] == 'э' or word[i] == 'е' or word[i] == 'ы' or word[i] == 'ё' or word[i] == 'я' or word[i] == "ю":
            countofvowel+=1
    return countofvowel
vinnilyricinlist = list(map(countvowelinwotd, vinnilyricinlist))
print(vinnilyricinlist)
def vvinyliric(func, list_obj: list) -> bool:
    result = []
    for obj in list_obj:
        result.append(func(obj))
    if len(set(result)) == 1:
        return True
    return False
if vvinyliric(lambda x: x==vinnilyricinlist[0], vinnilyricinlist) == True:
    print ('Парам-пам-пам')
else:
    print ('Пам парам')
    
        
        
    
    



    