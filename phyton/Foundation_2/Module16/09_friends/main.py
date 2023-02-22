deb_list = []
friend_nums = int(input("Количество друзей: "))
friends_list = [0 for _ in range(friend_nums)]
deb_nums = int(input("Количество долговых расписок: "))

for i in range(deb_nums):
    print()
    print(f'{i+1}-я расписка')
    whom = 0
    frome =0
    while whom == frome:
        whom = int(input("Кому: "))
        frome = int(input("От кого: "))
    deb_list.append([whom, frome, int(input("Сколько: "))])
print()
print("Баланс друзей:")
for deb in deb_list:
    friends_list[deb[0]-1] -= deb[2]
    friends_list[deb[1]-1] += deb[2]
for i in range(friend_nums):
    print(f'{i+1}: {friends_list[i]}')
print()