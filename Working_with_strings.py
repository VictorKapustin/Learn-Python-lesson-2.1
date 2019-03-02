# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'
print(len(word))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'уеыаоэяию'
print(sum(1 for i in word.lower() if i in vowels ))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
print(sum(len(word) for word in sentence.split())/len(sentence.split()))
