person = {"name": "Bowen", "age": 30, "city": "Winnipeg"}
print(person["name"])

person = {"first_name": "yong", "last_name": "xue", "age": 30, "city": "winnipeg"}
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

favorite_numbers = {
    "bowen": 7,
    "lumia": 3,
    "fei": 8,
    "nemo": 1,
    "amy": 9,
}
print("Bowen 的幸运数字是 " + str(favorite_numbers["bowen"]))

glossary = {
    "variable": "存东西的盒子",
    "string": "文字",
    "list": "一排排好的东西",
    "tuple": "不能改的列表",
    "loop": "重复做一件事",
}
print("variable: " + glossary["variable"])
print("string: " + glossary["string"])

for word, meaning in glossary.items():
    print(word + ": " + meaning)

    rivers = {"nile": "egypt", "amazon": "brazil", "yangtze": "china"}
for river, country in rivers.items():
    print(river + " 流经 " + country)
print(rivers.keys())     # 所有河流
print(rivers.values())   # 所有国家

poll = {"bowen": "yes", "lumia": "no"}
people = ["bowen", "lumia", "fei"]
for person in people:
    if person in poll:
        print("谢谢 " + person + "，你已经投过票了")
    else:
        print(person + "，请来投票！")
people = [{"name": "bowen", "age": 30, "city": "winnipeg"},
{"name": "lumia", "age": 28, "city": "toronto"},]
for person in people:
    print(person["name"] + " 住在 " + person["city"])

cars = [{"brand": "BMW" , "price": "70000 dollars"},
    {"brand" : "Honda", "price" : "50000 dollars"}]
for car in cars :
    print (car["brand"] + " costs " + car["price"])

pets = [
    {"name": "wangcai", "kind": "dog", "owner": "bowen"},
    {"name": "mimi", "kind": "cat", "owner": "lumia"},
]
for pet in pets:
    print(pet["name"] + " 是一只 " + pet["kind"])

favorite_places = {
    "bowen": ["tokyo", "paris"],
    "lumia": ["beijing"],
}
for name, places in favorite_places.items():
    print(name + " 喜欢的地方：")
    for place in places:
        print("  - " + place)
favorite_numbers = {
    "bowen": [7, 13],
    "lumia": [3, 9],
}
for name, numbers in favorite_numbers.items():
    print(name + " 的幸运数字是 " + str(numbers))

cities = {
    "tokyo": {"country": "japan", "population": 14000000},
    "paris": {"country": "france", "population": 2100000},
}
for city, info in cities.items():
    print(city + " 在 " + info["country"] + "，人口 " + str(info["population"]))

