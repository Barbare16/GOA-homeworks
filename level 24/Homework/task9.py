'''შექმენით პროგრამა while ციკლით რომელიც მომხარებელს შეეკითხება რიცხვებს სანამ ის არ შემოიყვანს რომელიმე რიცხვს 0-იდან 10-მდე'''

number = int(input('Guess the number: '))
while number < 0 or number > 10:
    number = int(input('Try again: '))
print('You have guessed the number!')
