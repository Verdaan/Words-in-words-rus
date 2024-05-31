from itertools import permutations
import re

print("Введите слово от 2 до 8 букв:")
input_word = input()
original_word = input_word.lower()
print("Загрузка. . .")

final_word_list = []
fixed_word_list = []

with open("rus_words.txt", "r", encoding="utf-8") as f:
    word_list = f.readlines()                                  #Слова в списке имеют на конце "\n", которые надо убрать
    for words in word_list:
        if words[0] not in original_word:                        #Убираем очевидно неподходящие слова, снижая нагрузку на память
            continue
        else:
            fixed_words = re.sub('\n', '', str(words))
            fixed_word_list.append(fixed_words)


set_of_letters = list(permutations(original_word))


if original_word in fixed_word_list:
    for i in set_of_letters:
        final_word = ""
        mid_word = ""
        if i[0] == "ь" or i[0] == "ъ" or i[0] == "ы":
            continue
        for k in range(2, len(original_word) + 1):
            for j in i:
                mid_word += j                            #mid_word - промежуточное слово
            final_word = mid_word[:k]                    #final_word - окончательное слово
            if final_word in final_word_list or final_word == original_word:
                continue
            else:
                if final_word in fixed_word_list:
                    final_word_list.append(final_word)
                else: continue
else: print("Такого слова нет в словаре")

if final_word_list == []:
    print("Из этого слова невозможно собрать другие")
else:
    print(final_word_list)
