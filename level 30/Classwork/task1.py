'''1) შექმენით პროგრამა რომელიც შეამოწმებს მოსწავლის ქულას (რომელსაც მიიღებს input-ის საშვალებით) თუ ქულა მეტია 50-ზე შეამოწმეთ მეტია თუ არა 75-ზე მაშინ დაბეჭდეთ "A" სხვა შემთხვევაში კი "B" თუ ქულა არაა მეტი 50-ზე მაშნ შეამოწმეთ მეტია თუ არა 25-ზე თუ მეტია დაბეჭდეთ "C" სხვა შემთხვევაში "D"'''

score = int(input('Enter your score'))
if score > 50:
    if score > 75:
        print('A')
    else:
        print('B')
elif score < 50:
    if score < 25:
        print('C')
    else:
        print('D')