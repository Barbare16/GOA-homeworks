''' მომხმარებელს იქამდე შეეკითხეთ რიცხვები სანამ უარყოფით რიცხვს არ შემოიყვანს, while ციკლისა და input ინსტრუქციის საშვალებით, ასევე პირობითი განცხადებების დადებითობა/უარყოფითობის შესამოწმებლად, საბოლოოდ დაბეჭდეთ ყველა მიღებული დადებითი რიცხვის ჯამი'''

total = 0
number = int(input('Enter a Ngeative number '))
while number >= 0:
    if number > 0:
        total += number
    number = int(input('Number is not Negative '))
print('The sum of your positive numbers: ' + str(total))