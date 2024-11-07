'''მომხმარებელს შემოატანინეთ თავისი სახელი, გვარი, ასაკი და ქალაქი. შემდეგ ეს ინფორმაცია ერთ წინადადებად დაუბეჭდეთ ტერმინალში'''

#მომხმარებელს შემოვატანინე თავისი სახელი
first_name=input('enter your first name: ')
#მომხმარებელს შემოვატანინე თავისი გვარი
last_name=input('enter your last name: ')
#მომხმარებელს შემოვატანინე თავისი ასაკი
age=input('enter your age: ')
#მომხმარებელს შემოვატანინე ქალაქის სახელი სადაც ის ცხოვრობს
town=input('enter the name of the town where you live: ')

#მთელი ეს ინფორმაცია ჩავსვი წინადადებებში
print('Hi ' + first_name + ' ' + last_name + '!.  you are ' + age + ' years old. we will find english teacher for your age who will be able to teach you in ' + town + ' finding the teacher may take 3 days.' )
