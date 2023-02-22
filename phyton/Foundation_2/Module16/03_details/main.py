shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
unit_list = []
unit_count, unit_cost = 0, 0
for unit in shop:
    if not unit[0] in unit_list:
        unit_list.append(unit[0])
print("Товары в магазине:", unit_list)
cur_unit = input("Название детали: ")
for shop_unit in shop:
    if cur_unit in shop_unit:
        unit_count +=1
        unit_cost += shop_unit[1]
print("Кол-во деталей —", unit_count)
print("Общая стоимость —", unit_cost)