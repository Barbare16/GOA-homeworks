'''2) შექმენით პროგრამა, რომელშიც მომხმარებელს შემოატანინებთ ქულას, შემდეგ კი if განხადების საშვალებით გამოუტანთ 2 შესაძლო შედეგს: "You have passed" ან "You failed"'''
score = int(input('Enter your score '))
if score >= 100:
    print('You have passed!')
if score < 100:
    print('You failed')