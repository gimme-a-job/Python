import person

person1 = person.Person('太郎', '東京', 150, 200, 150)
person2 = person.Person('次郎', '大阪', 200, 190, 100)
person3 = person.Person('三郎', '名古屋', 100, 180, 90)

print(f'{person1.last_name}{person1.first_name}さんのBMIは{person1.bmi():.2F}です。')
print(f'{person2.last_name}{person2.first_name}さんのBMIは{person2.bmi():.2F}です。')
print(f'{person3.last_name}{person3.first_name}さんのBMIは{person3.bmi():.2F}です。')