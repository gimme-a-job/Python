# 5.4 if文による分岐

# FizzBuzzプログラムの作成を作成してください。
# "https://ja.wikipedia.org/wiki/Fizz_Buzz"より
for i in range(1, 100+1):
    str = ""
    if i%3 == 0: str += "Fizz"
    if i%5 == 0: str += "Buzz"
    if str == "":  str = i
    
    if i%10 != 0: print(str, end=", ")
    else: print(str)

num = int(input('整数を入力してね : '))
str2 = ""
if num%3 == 0: str2 += "Fizz"
if num%5 == 0: str2 += "Buzz"
if str2 == "":  str2 = "反応がない、しかぱねのようだ"
print('ホアンからのお告げは「%s」'%str2)

# うるう年判定プログラムを作成してください。
year = int(input('西暦を入力しな！ : '))
# "https://www.geekpage.jp/programming/c/leap-year.php"より
if year%4==0:
    if year%100==0:
        if year%400==0: print('うるう年です')
        else: print('うるう年ではありません')
    else: print('うるう年です')
else: print('うるう年ではありません')

# BMI判定プログラムを作成してください。
#5.2より
# リスト内包表記を使用して、BMIの値を計算してください。BMIはタプルの入れ子（((170, 70), (180, 100))で表現）とします。
tuple_hw = ((170, 70), (180, 1000))
list_BMIs = [hw[1]/((hw[0]/100)**2) for hw in tuple_hw]
print(list_BMIs)

def judgeBMI(bmi):
    list_strsBMI = ((0, "痩せすぎ"), (16, "痩せ"), (17, "痩せぎみ"), (18.5, "普通体重"), (25, "前肥満"), (30, "肥満(1度)"), (35, "肥満(2度)"), (40, "肥満(3度)"))
    str = ""
    for tuple in list_strsBMI:
        if tuple[0] < bmi: str=tuple[1]
        else: break
    return str

for j in range(len(tuple_hw)):
    print('身長%icm、体重%ikgの場合、ぶっちゃけ「%s」ですね'%(tuple_hw[j][0], tuple_hw[j][1], judgeBMI(list_BMIs[j])))

height = int(input('貴様の身長をセンチみーたーで入力しろ! : '))
weight = int(input('で、体重は？ : '))
print('身長%icm、体重%ikgの場合、ぶっちゃけ「%s」だな'%(height, weight, judgeBMI(weight/((height/100)**2))))