'''2) შექმენით ცვლადი რომელშიც შეინახავთ თქვენს სახელს დიდი ასოებით, შემდეგ შექმენით ახალი ცვლადი new_name რომელშიც თქვენი სახელი ეწერება პატარა ასოებით, ჯერ გამოიყენეთ for ციკლი და if. შემდეგ კი გააკეთეთ ეს lower მეთოდით'''

Name = 'BARBARE'
New_name = ''
# for ციკლი
for char in Name:
    if char == 'B':
        New_name += 'b'
    if char == 'A':
        New_name += 'a'
    if char == 'R':
        New_name += 'r'
    if char == 'E':
        New_name += 'e'
print(New_name)
# .lower ფუნქციით:
print(Name.lower())
    
