import math

# 5.2 for文による繰り返し処理

# 5回繰り返す処理を記述してください。繰り返し回数を表示してください。
for i in range(5): print('%i 回繰り返しました'%(i+1))

# 1～100まで合計を求めてください。
sum = 0

for i in range(1,100+1):
    sum +=i

print(sum)

# for文とrangeクラスを使用して、2～100までの間の偶数を表示してください。
list1 = []

for i in range(2, 100+1):
    if i%2==0: list1.append(i)

print(list1)

# for文の入れ子を使用して九九の表を表示してください。
list99 = []

for i in range(1, 9+1):

    list_temp = []

    for j in range(1, 9+1): list_temp.append(i*j)

    list99.append(list_temp)

    print(list99[i-1])

print(list99)

# *で三角形を描画してください。
bottom = 9
midpoint = math.ceil(bottom/2) #切り上げ

list_triangle = []
for i in range(0, midpoint):
    list_temp = []
    for j in range(bottom): list_temp.append(" ")
    for j in range(midpoint-i-1, midpoint+i-1+1): list_temp[j] = "*"
    # print(list_temp)
    list_triangle.append(list_temp)
    # print(list_triangle[i], sep="")

# print(*list_triangle, sep="")
for row in list_triangle: print(*row)

# リストの要素をfor文で表示してください。
for row in list_triangle: print(*row, sep=", ")

# リスト['Tokyo', 'Osaka', 'Nagoya']の要素をfor文で表示してください。
cities = ['Tokyo', 'Osaka', 'Nagoya']
for city in cities: print(city)

# 文字列のリストに含まれる各文字列の長さを表示してください。
list_strings = []
list_strings.append("ホアンさんはよくいびきをかきます。")
list_strings.append("ハマノさんはfxが大好きです。")
for str in list_strings: print("文字列「%s」の長さは : %i"%(str, len(str)))

# リストの要素の最大値とその前後1つずつのデータを表示してください。


# リスト内包表記を使用して、1～5の数字のリストを作成して表示してください。
list15 = [i for i in range(1, 5+1)]
print(list15)

# リスト内包表記を使用して、半径が1～5の円の面積を表示（円周率は3.14を使用）してください。
list_circles = [i*i*3.14 for i in list15]
print(list_circles)

# リスト内包表記を使用して、BMIの値を計算してください。BMIはタプルの入れ子（((170, 70), (180, 100))で表現）とします。
tuple_hw = ((170, 70), (180, 100))
list_BMIs = [hw[1]/((hw[0]/100)**2) for hw in tuple_hw]
print(list_BMIs)