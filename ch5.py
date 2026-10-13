users = []
if users:
    print("有人")
else:
    print("我们需要找些用户来！")

current_users = ["bowen", "lumia", "fei"]
new_users = ["Fei", "nemo", "Amy"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + " 已被占用，换一个吧")
    else:
        print(new_user + " 可以用")

numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")