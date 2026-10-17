sandwich_orders = ["tuna", "club", "veggie"]
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("正在做 " + sandwich + " 三明治")
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)

sandwich_orders = ["pastrami", "tuna", "pastrami", "club", "pastrami"]
print("pastrami 卖完了")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)

responses = {}
while True:
    name = input("你叫什么名字？（输入 quit 退出）")
    if name == "quit":
        break
    place = input("你梦想中的度假地是哪里？")
    responses[name] = place
for name, place in responses.items():
    print(name + " 想去 " + place)