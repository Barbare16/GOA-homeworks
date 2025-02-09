'''შექმენით პროგრამა რომელიც მომხმარებელს შეეკითხება პაროლს სანამ ის არ შემოიყვანს goabest123-ს'''

password = input('Enter the password: ')
while password != 'goabest123':
    print('password inncorrect!')
    password = input('Enter the password: ')
print('Password is correct!')