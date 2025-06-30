'''1) შექმენით ფუნქცია multiply რომელსაც გადაეცემა ორი რიცხვი და ის დააბრუნებს მათ ნამრავლს. ფუნქცია გამოიძახეთ 3-ჯერ და დაბრუნებული შედეგები შეინახეთ product1, product2 და product3 ცვლადებში'''

def multiply(a , b):
    return(a * b)

product1 = (multiply(1 , 5))
product2 = (multiply(product1 , 2))
product3 = (multiply(product2 , 2))

print(product1)
print(product2)
print(product3)