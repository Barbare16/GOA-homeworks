'''მომხმარებელს შემოატანინეთ ასაკი დაუმატეთ 5 და შემდეგ დაუბეჭდეთ წინადადება ასეთ ფორმატში: 'You will be <ასაკი> years old after 5 years '''

# მომხმარებელს შემოვაყვანინე მისი ასაკი
Users_age1 = int(input('please enter your age: '))
#  გამოვთვალე თუ რამდენი წლის იქნება ხუთ წელში
Users_age2 = Users_age1 + 5
 
# დავუბეჭდე წინადადება რომელიც ეუბნება საბოლოო პასუხს
print('you will be ' + str(Users_age2) + ' years old in 5 years')