''' შექმენით პროგრამა რომელიც მომხმარებლისგან მიიღებს რიცხვს, შემდეგ დაადგენს დადებითია, უარყოფითი თუ ნული if-elif-else ის საშვალებით, თუ რიცხვი დადებითია შეამოწმეთ არის თუ არა ლუწი თუ არის დაბეჭდეთ "The number is positive and even." ხოლო სხვა შემთხვევაში დაბეჭდეთ "The number is positive and odd."'''

number = int(input('Enter a number'))
if number > 0:
    if number % 2 == 0:
        print('The number is positive and even')
    else:
        print('Number is Positive and even')
elif number < 0:
    print('Number is negative')
else:
    print('The number is neither positive nor negative.')
