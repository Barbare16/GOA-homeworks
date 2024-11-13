''' მომხმარებელს შემოტანინენთ სახელი, გვარი, ასაკი, ემაილი, პაროლი და თქვენთვის საინტერესო კიდევ 2 მონაცემი, შემდეგ შეინახეთ ცვლადში და საბოლოოდ დაბეჭდეთ ინფორმაცია ერთ დიდ წინადადებაში'''

# მომხმარებელს შემოვატანინე თავისი სახელი
Users_first_name = input('please enter your first name: ')
# მომხმარებელს შემოვატანინე თავისი გვარი
Users_last_name = input('please enter your last name: ')
# მომხმარებელს შემოვატანინე თავისი ასაკი
Users_age = input('please enter your age: ')
# მომხმარებელს შემოვატანინე თავისი იმეილი
Users_email = input('please enter your email: ')
# მომხმარებელს შემოვატანინე თავისი პაროლი
Users_password = input('please enter your pasword: ')
# მომხმარებელს შემოვატანინე თავისი სახლის მისამართი
Users_home_adress = input('please enter your home adress: ')
# მომხმარებელს შემოვატანინე თავისი ტელეფონის ნომერი
Users_phone_number = input('please enter your phone number: ')
# მომხმარებელს შემოვატანინე თავისი იუზერნეიმი
Users_username = input('please enter your username.(everyone can see it): ')


#ახლა ეს ყველა მომხმარებლისგან შემოტანილი ინფორმაცია უნდა მოვათავსო ერთ დიდ წინადადებაში
print('Hello '+ Users_first_name + ' ' + Users_last_name+' ! you are '+ Users_age + ' (3+)years old. so you successfully signed in on our online shopping website as '+ Users_username + ' your password is '+ Users_password + ' and dont forget it! anything that you will buy something on our website will be sent on '+ Users_home_adress + ' . Before one day of giving you your order, we will sned you a message on phone number (' + Users_phone_number + 'and also we will send a message on gmail( ' + Users_email + ' . If you want to change your phone number, username and so on, go to the settings and click my profile,and then edit profile. dont forget to rate us! Enjoy!')
