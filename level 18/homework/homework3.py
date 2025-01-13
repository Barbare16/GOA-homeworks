'''მომხმარებელს შემოატანინეთ მასზე ინფორმაცია და ეს ყველაფერი ერთ print-ში დაბეჭდეთ'''
# მომხმარებელს შემოვატანინე მისი სახელი
users_name = input('Enter your username: ')
# მომხმარებელს შემოვატანინე თუ მერამდენე ლეველზე
users_level = input('Enter your level: ')
# მომხმარებელს შემოვატანინე თუ რამდენი ვარსკვლავი აქვს აგროვებული
collected_stars = input('Enter the number of stars you have collected: ')
# ყველაფერს ორ წინადადებაში ვბეჭდავ
print(users_name + ' is on level ' + users_level + '. ' + users_name + ' has collected ' + collected_stars + ' stars')