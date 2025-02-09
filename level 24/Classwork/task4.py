'''3) მომხმარებელს შეეკითხეთ სახელი და იქამდე არ შეეშვათ (განმეორებითად ჰკითხეთ) სანამ თქვენს სახელს არ შემოიყვანს'''
name = input('Guess my name: ')
while name != 'Barbare':
    print('Try again!')
    name = input('Guess my name: ')
print('You have guessed my name!')

