'''3) თქვენი სახელის სტრინგზე გამოიყენეთ მეთოდები: lower, upper, capitalize და დაბეჭდეთ. შემდეგ მოიყვანეთ .find მეთოდზე 3 მაგალითი თითოეულზე განსხვავებული შემთხვევით: მოიძნება, ვერ მოიძებნა, გამოიტანა error'''

Name = 'BaRbArE'
# lower (პატარა ასოები)
print(Name.lower)
# Upper (დიდი ასოები)
print(Name.upper)
# Capitalize (მხოლოდ პირველი ასოს გადიდება)
print(Name.capitalize)
# .find
print(Name.find('R')) # მოიძებნა (სტრინგში არის ეს ასო)
print(Name.find('H')) # ვერ მოიძებნა (ეს ასო სტრინგში არ არის)
print(Name.find()) # error (მეთოდს საბუთი სჭირდება)