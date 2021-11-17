def merge(*lists):
    new_lists = []
    for list in lists:
        new_lists.extend(list)
    return sorted(new_lists)


while True:
    lists = []
    k = int(input('Введите k = '))
    for i in range(k):
        print(i+1, " список (введите значения списка через пробел): ")
        nums = [int(i) for i in input('nums = ').split()]
        lists.append(nums)

    print("Вывод: ", list(merge(*lists)))
