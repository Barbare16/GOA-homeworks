'''5) მომხმარებელს 3 მცდელობა აქვს სწორი PIN კოდის შეყვანისთვის. თუ შეიყვანს სწორად, დაიბეჭდება "Access Granted", სხვა შემთხვევაში "Access Denied" გამოიყენეთ პირობითი განცხადებები'''

PIN = '123'
guess = input('Enter your pin: ')
attempts = 2
while attempts > 0:
    if guess == PIN:
        print('Access Granted!')
        attempts = 0
    elif guess != PIN:
        guess = input('Try again: ')
        attempts -= 1
if guess != PIN:
    print('Access Denied')