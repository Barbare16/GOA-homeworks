'''გააკეთეთ 5-5 მაგალითი თთოეულ შედარების ოპერატორზე (>, >=, <, <=, ==, !=), გვერდზე კომენტარის საშვალებით მიუთითეთ თუ რომელ boolean მნიშვნელობას გამოიტანას, აიღეთ მრავალფეროვანი კომბინაციები, შეეცადეთ გქონდეთ ყველა ვარიანტი'''

# > ოპერატორი
print(10 > 9.9 ) # True
print(21 > 22) # False
print(4 > 4) # False
print(5 > -5) # True
print(3 > 10) # False

# >= ოპერატორი
print(10 >= 9.9) # True
print(22 >= 23) # False
print(10 >= 10) #True
print(-50 >= 50) # False
print(10 >= 1) # True

# < ოპერატორი
print(1 < 2) # True
print(1 < 1) # False
print(-1 < 1) # True
print(1 < -1) # False
print(3 < 2.9) # False

# <= ოპერატორი
print(1 <= 2) # True
print( 5 <= 1) # False
print( 1 <= -1) #False
print(9.9 <= 10) # True
print(10 <= 10) # True

# == ოპერატორი
print(90 == 90) # true
print(20 == 40) # False
print(40 == 20) #False
print(20 == -20) #False
print(20.1 == 20.3) #False

# != ოპერატორი
print(90 != 90) # False
print(20 != 40) # True
print(40 != 20) # True
print(20 != -20) # True
print(20.1 != 20.3) # True