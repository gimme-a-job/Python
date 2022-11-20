# 5.5 端末からの入力
# 入力された名前を表示してください。
name = input('名前を入力してください : ')
print(name)

# 姓と名を別々に入力して、その後、氏名を表示してください。
name_family = input('苗字を入力してね : ')
name_given = input('下の名前を入力してね : ')
print('君の名は…%s %s だね'%(name_family, name_given))

# 2つの整数を入力し、四則演算を行い画面に表示してください。
num1 = int(input('数字１ : '))
num2 = int(input('数字２ : '))
print('%i と %i を足すと %i だね'%(num1, num2, num1+num2))
print('%i から %i を引くと %i だね'%(num1, num2, num1-num2))
print('%i と %i を掛けると %i だね'%(num1, num2, num1*num2))
print('%i と %i で割ると %f だね'%(num1, num2, num1/num2))

# 身長と体重を入力し、BMIの結果を表示してください。
#chap5.4.pyより
def judgeBMI(bmi):
    list_strsBMI = ((0, "痩せすぎ"), (16, "痩せ"), (17, "痩せぎみ"), (18.5, "普通体重"), (25, "前肥満"), (30, "肥満(1度)"), (35, "肥満(2度)"), (40, "肥満(3度)"))
    str = ""
    for tuple in list_strsBMI:
        if tuple[0] < bmi: str=tuple[1]
        else: break
    return str

height = int(input('貴様の身長をセンチみーたーで入力しろ! : '))
weight = int(input('で、体重は？ : '))
print('身長%icm、体重%ikgの場合、ぶっちゃけ「%s」だな'%(height, weight, judgeBMI(weight/((height/100)**2))))



# （応用）1から50の間の数値を当てるプログラムを作成してください。入力された値が正解より大きいか、小さかを表示してください。正解までの繰り返し回数を表示してください。

#inputcheck.pyより

max, setval, min = 50, 25, 1 #'setval'は正解の値って意味のつもり

def input_int():

    while True:
     x = input("%i ~ %i で正の整数を入力してください : "%(min, max))
     try:
        x = int(x)
     except ValueError:
        print(x, "は整数に変換できません")
        continue
     except:
        print("予期していないエラーです")
        exit()
     if x <min:
        print(x, "は%iより少ないですよ"%min)
        continue
     if max <x:
        print(x, "は%iを超えちゃってますよ"%max)
        continue
      # 以下は正しい入力が得られた時の処理
     return x

count =0

while True:
    
    print('%i 回目の挑戦！'%(count+1))

    answer = input_int()

    if answer <setval: print('少ない')
    if setval <answer: print('大きい')
    if answer == setval:
        print('正解')
        break

    print() #見やすくなるかなと思った

    count +=1