'''მომხმარებელს შემოატანინეთ 2 რიცხვი, შემდეგ კი ამ ორ რიცხვს შორის არსებული ყველა რიცხვის ჯამი გაიგეთ for ციკლის გამოყენებით უმციერსიდან უდიდესამდე. საბოლოოდ დაბეჭდეთ ეს ჯამი'''

input1 = int(input('Enter a random number: '))
input2 = int(input('Enter one more number: '))
var1 = 0
for i in range ((input1 +1), input2 ):
    var1 += i