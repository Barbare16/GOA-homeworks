'''while ციკლის საშვალებით დაბეჭდეთ რიცხვები 0-იდან 20-მდე, შეამოწმეთ თითოეული რიცხვი ლუწია თუ კენტი, თუ ლუწია დაბეჭდეთ "even" თუ კენტია დაბეჭდეთ odd და გვერდზე მიუწერეთ ეს რიცხვი თითოეულ შემთხვევაში'''
counter = -1
while counter < 20:
    counter += 1
    if counter % 2 == 0:
        print(str(counter) + ' is even')
    else:
        print(str(counter) + ' is odd')