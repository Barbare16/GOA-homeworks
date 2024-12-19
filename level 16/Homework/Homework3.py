'''შექმენით პროგრამა, რომელიც განსაზღვრავს productive ცვლადის მნიშვნელობას შემდეგი პირობების მიხედვით:
read_pages ცვლადში ინახება წაკითხული გვერდების რაოდენობა (მთლიანი რიცხვი).
free_time ცვლადში ინახება boolean მნიშვნელობა (True/False), რომელიც გვიჩვენებს, ჰქონდა თუ არა თავისუფალი დრო.
productive ცვლადი იქნება ჭეშმარიტი (True), თუ მოსწავლემ წაიკითხა მინიმუმ 20 გვერდი და თავისუფალი დრო ჰქონდა.
მაგალითი: თუ read_pages = 25 და free_time = True, მაშინ productive = True.
თუ read_pages = 15 და free_time = True, მაშინ productive = False.
თუ read_pages = 30 და free_time = False, მაშინ productive = False.'''
 
read_pages = int(input('Enter how many pages u have read: ')) # შევქმენი read_pages ცვლადი რომელიც ინახავს მომხმარებლის მიერ წაკითხული გვერდების რაოდენობას
free_time = bool(input('Do you have free time?: '))  # შევქმენი free_time ცვლადი რომელიც ინახავს ჰქონდა თუ არა მომხმარებელს თავისუფალი დრო

productive = (read_pages >= 20 ) and free_time  # შევქმენი productive ცვლადი რომელიც ამოწმებს მომხმარებელს ჰქონდა თუ არა წაკითხული მინიმუმ 20 გვერდი და ჰქონდა თუ არა თავისუფალი დრო. ამ ორ ინფორმაციას შორის სრულდება and ლოგიკური ოპერაცია. საბოლოო პასუხით გამოჩნდება არის თუ არა მომხმარებელი პროდუქტიული

print('The fact that you are productive is ' + str(productive) )
 