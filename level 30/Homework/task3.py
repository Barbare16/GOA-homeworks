'''4) შექმენით პროგრამა რომელშიც მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ უარყოფითს არ შეიყვანს. დაბეჭდეთ შეყვანილი ლუწი და კენტი რიცხვების რაოდენობა გამოიყენეთ პირობითი განცხადებები'''
odd = 0
even = 0
number = int(input('Enter a number'))
while number >= 0:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print('You entered odd number ' + str(odd) + ' times, and you entered even number ' + str(even) + ' times')