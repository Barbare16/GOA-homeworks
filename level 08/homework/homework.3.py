''' შექმენით 10 string ტიპის და 10 ინტეჯერ ტიპის ცვლადი, გააკეთეთ 5 კონკატინაციისა (სტრინგების შეერთების) და 5 მათემატიკური ჯამის მაგალითი'''
# ვქმნი ათ ცვლადს რისი მნიშვნელობის ტიპი სტრინგია
str_1='foot'
str_2='ball'
str_3='5'
str_4='10'
str_5='Barbare '
str_6='Shaverdashvili'
str_7='Hello '
str_8='world'
str_9='100'
str_10='50'
# ვქმნი ათ ცვლადს რისი მნიშვნელობის ტიპი ინტეჯერია
int_1=2
int_2=3
int_3=6
int_4=4
int_5=10
int_6=5
int_7=123
int_8=77
int_9=100
int_10=50
# ახლა ვაკეთებ ხუთ კონკატინაციის მაგალითს ცვლადების დამატებით
# პრინტით გამომაქვს სტრინგი-'football'
print(str_1 + str_2)
# პრინტით გამომაქვს სტრინგი-'510'
print(str_3 + str_4)
# პრინტით გამომაქვს სტრინგი-'Barbare Shaverdashvili'
print(str_5 + str_6)
# პრინტით გამომაქვს სტრინგი-'Hello world'
print(str_7 + str_8)
# პრინტით გამომაქვს სტრინგი-'10050'
print(str_9 + str_10)

# ახლა ვაკეთებ ხუთ მათემატიკურ ჯამის მაგალითს ცვლადებით
# პრინტით გამომაქვს ინტეჯერი-5
print(int_1 + int_2)
# პრინტით გამომაქვს ინტეჯერი-10
print(int_3 + int_4)
# პრინტით გამომაქვს ინტეჯერი-15
print(int_5 + int_6)
# პრინტით გამომაქვს ინტეჯერი-200
print(int_7 + int_8)
# პრინტით გამომაქვს ინტეჯერი-150
print(int_9 + int_10)

#დასკვნა:თუ გვინდა რაიმე რიცხვის ერთმანეთისთვის მიმატება,თუ ამ რიცხვებს აქვს ბრჭყალები,ანუ თუ ეს რიცხვი სტრინგია,მიმატებისას არ მოხდება მათემატიკური შეკრება,ამის მაგივრად ისინი "ერთმანეთის გვერდით" დადგებიან,თუ გვინდა რომ მოხდეს მათემატიკური შეკრება,ამისთვის რიცხვს უნდა მოვაშოროთ ბრჭყალები. ტექსტს რომელიც სიტყვიერია,უნდა დავუწეროთ ბრჭყალები,თუ არ დავუწერთ ერორი იქნება.როგორც ვთქვი სტრინგების ერთმანეთთან მიმატება შეიძლება მაგრამ არა მათემატიკური შეკრება. აი სიტყვაზე თუ ამ ორ სტრინგს 'butter'ს და  'fly' ს ერთმანეთს მივუმატებთ, პასუხად მივიღებთ butterfly ს
