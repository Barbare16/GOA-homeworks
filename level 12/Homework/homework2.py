'''მარტივი გამომთვლელი: შექმენით პროგრამა რომელიც მომხმარებელს შემოატაინინებს 2 რიცხვს და შეინახავს ცვლადებში, გარდაქმენით ეს რიცხვები integer-ად, შემდეგ კი დაბეჭდეთ მათ შორის 4 მათემატიკური ოპერაცია (+,-,*,//)'''

#  მომხმარებელს უნდა შემოვატანინო რაიმე რიცხვი რომელსაც ინტეჯერად გარდავქმნი და შემდეგშევინახავ ცვლადში სახელად Number1
Number1 = int(input('please enter a number: '))
#  მომხმარებელს უნდა შემოვატანინო რაიმე რიცხვი რომელსაც ინტეჯერად გარდავქმნი და შემდეგშევინახავ ცვლადში სახელად Number2
Number2 = int(input('please enter a number: '))

# Number1 და Number2 ცვლადებს ერთმანეთს ვუმატებ
print(Number1 + Number2)
# Number1 და Number2 ცვლადებს ერთმანეთს ვაკლებ
print(Number1 - Number2)
# Number1 და Number2 ცვლადებს ერთმანეთზე ვამრავლებ
print(Number1 * Number2)
# Number1 და Number2 ცვლადებს ერთმანეთზე ვყოფ
print(Number1 // Number2)