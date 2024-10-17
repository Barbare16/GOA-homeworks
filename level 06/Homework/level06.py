'''შექმენით 5 ცვლადი რომლებშიც შეინახავთ წიგნების თავდაპირველ ფასს, შემდეგ შექმენით ცვლადი რომელშიც შეინახავთ ფასდაკლების ოდენობას, შექმენით ახალი ფასის მქონე წიგნების ცვლადები, რომელთა მნიშვნელობა იქნება ძველ მნიშვნელობას გამოკლებული ახალი, საბოლოოდ კი დაბეჭდეთ ახალი წიგნების ფასები (გამოიყენეთ დღეს ნასწავლი მასალა და საუკეთესო პრაქტიკები: გამოიყენეთ ის რომ ცვლადის მნიშვნელობის მინიჭებისას შეგიძლიათ სხვა ცვლადის გამოყენება, კოდი ახსენით კომენტარების საშვალებით, ცვლადებს დაარქვით აღმწერი სახელები snake_case-ის სტილში)'''

#ვქმნი 5 ცვლადს რომლის ახელიც იქნება წიგნის სახელი,ხოლო მნიშვნელობა ამ წიგნის ფასი(ლარებში).
Harry_Potter=45
The_Little_Prince=25
Sherlock_Holmes=30
Don_Quixote=15
The_Lord_of_the_Rings=40
#ახლა ვქმნი ცვადს,სადაც შევინახავ თუ რამდენი ლარი შეიძლება დააკლდეს წიგნს ფასდაკლების დროს.
sale1=23
sale2=10
sale3=15
sale4=5
sale5=20

#ახლა შევქმნი ცვლადს,რისი მნიშვნელობაც იქნება გაახლებული წიგნის ფასები ფასდაკლებით
New_price_of_Harry_Potter=Harry_Potter-sale1
New_price_of_The_little_prince=The_Little_Prince-sale2
New_price_of_Sherlock_Holmes=Sherlock_Holmes-sale3
New_price_of_Don_Quixote=Don_Quixote-sale4
New_price_of_The_lord_of_the_rings=The_Lord_of_the_Rings-sale5

#ახლა კი დავბეჭდავ საბოლოო წიგნის ფასებს
print(New_price_of_Harry_Potter)
print(New_price_of_Sherlock_Holmes)
print(New_price_of_Don_Quixote)
print(New_price_of_The_lord_of_the_rings)