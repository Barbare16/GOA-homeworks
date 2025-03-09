''' მომხმარებელს შემოატანინეთ ქულა score და შეინახეთ ცვლადში, როგორც integer.
შემდეგ, ქულის მიხედვით განსაზღვრეთ შეფასება (grade):
A. თუ score მეტია 80-ზე
B. თუ score მეტია 60-ზე
C. თუ score მეტია 40-ზე
D. თუ score მეტია 20-ზე
F. თუ score 20-ზე ნაკლებია'''

score = int(input('Enter your score: '))
if score >= 80:
    print('your grade is  A')
if score >= 60 and score < 80:
    print('Your grade is B')
if score >= 40 and score < 60:
    print('Your grade is C')
if score >= 20 and score < 40:
    print('Your grade is D')
if score < 20:
    print('Your grade is F')