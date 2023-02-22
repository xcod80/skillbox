def check_simetry(nums):
    for i in range(len(nums)//2):
        if nums[i] != nums[-(i+1)]:
            return False
    return True

nums = int(input("Количество чисел: "))
num_list = [int(input("Число:")) for _ in range(nums)]
check_list = []
check_list.extend(num_list)
i = 1
while not check_simetry(check_list):
    extend_list = num_list[:i][::-1]
    check_list = []
    check_list.extend(num_list)
    check_list.extend(extend_list)
    i += 1

print("Последовательность:", num_list)
print("Нужно приписать чисел:", len(extend_list))
print("Сами числа:", extend_list)