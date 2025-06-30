'''6) მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ -1-ს არ შეიყვანს. საბოლოოდ გამოიანგარიშოს შეყვანილი რიცხვების საშუალო'''
count = 0
sum = 0
guess = int(input('Enter a number --> '))
while guess != 1:
    sum += guess
    count += 1
    average = sum / count
    guess = int(input('Try again -->'))
print('The average of numbers you entered is: ' + str(average))