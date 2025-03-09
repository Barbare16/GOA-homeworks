'''5 შექმენით პაროლის ცვლადი და შეინახეთ თქვენთვის სასურველი სიტყვა, შემდეგ მომხმარებელს შეეკითხეთ პაროლი და შეინახეთ ცვლადში, იქამდე შეეკითხეთ სანამ სწორად არ ჩაწერს while ციკლით გამოყენებით, საბოლოოდ კი დაუბეჭდეთ "Logged in successsfuly" ასევე ის თუ რამდენი ცდა დასჭირდა, ამისთვის ცალკე ცვლადი შექმენით და ყოველ ციკლის გამეორებაზე გაზარდეთ 1-ით'''
attempts = 1
password = 'Barbare123'
user_input = input('Enter a password: ')
while user_input != password:
    attempts += 1
    user_input= input('Try again: ')
print('Logged in successfuly')
print('count of attempts: ' + str(attempts))