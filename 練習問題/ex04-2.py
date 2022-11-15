# 4.8
#
i = list(range(1, 10))
i.append(10)
print(i)

#
i = []
i.append('Tokyo')
i.append('Kanagawa')
i.append('Saitame')
print(i)

#
list_first = list(range(1, 6))
list_second = list(range(6, 11))
list_first.extend(list_second)
list_all = list_first
# list_all = list_first.extend(list_second)
print(list_all)

# 4.9
#
list1 = [1, 2, 3, 4, 5]
list2 = list1
list1[-1] = 0
list2[0] = 0
print(list1)
print(list2)

#
list1 = [[1, 2], [3, 4], [5, 4]]
list2 = list1.copy()
list1[0,0] = 0
list2[-1] = 10
print(list1)
print(list2)

# 4.14
#
t = (0, 'Tokyo')
t[0] = 1
print(t)

#
t = ('愛知', '名古屋', 22960000)
print(t)
#
t = {"神奈川": "横浜"}
print(t)
t["千葉"] = "千葉"
print(t)
print(t["神奈川"], t["千葉"])
