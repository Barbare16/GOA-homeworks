'''შექმენით 1 ცვლადი, შემდეგ for ციკლის საშვალებით გაიგეთ ყველა რიცხვი 15-მდე და ყველა ეს რიცხვი დაამატეთ პირველად შექმნილ ცვლადში, საბოლოოდ დაბეჭდეთ ჯამი. შეასრულეთ იგივე while ციკლით'''

var1 = 10

for i in range(1,  16):
    print(i + var1)

counter = 1
while counter <= 15:
    var3 = var1 + counter
    counter += 1
    print(var3)