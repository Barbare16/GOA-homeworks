'''7) მომხმარებელს შემოაყვანინეთ წინადადება, შემდეგ for ციკლისა და პირობითი განცხადებების საშვალებით დაბეჭდეთ ჯერ ხმოვნების, შემდეგ კი თანხმოვნების რაოდენობა (ხმოვნებად ჩათვალეთ სიმბოლოები: a, e, i, o, u ხოლო სხვა ყველა თანხმოვნად)'''
sentence = input('enter a sentence --> ')
vowels = 0
consonants = 0
for letters in (sentence):
    if letters == 'a' or letters == 'e' or letters == 'i' or letters == 'o' or letters == 'u':
        vowels += 1
    elif letters != 'a' or letters != 'e' or letters != 'i' or letters != 'o' or letters != 'u':
        consonants += 1
print('There are ' +  str(vowels) + ' vowels and '+ str(consonants) + ' Consonants In your sentence')