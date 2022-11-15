import math

# 5.6 エラーへの対処

# 5人分の点数を入力します。点数が0未満、100を超えるときはエラーを表示して継続します。入力終了後に最高点、最低点と平均値を表示します。

#inputcheck.pyより


def input_int():

    while True:
     x = input("正の数値を入力してください : ")
     try:
        x = int(x)
     except ValueError:
        print(x, "は整数に変換できません")
        continue
     except:
        print("予期していないエラーです")
        exit()
     if x <0:
        print(x, "は正の数値ではありません")
        continue
     if 100 <x:
        print(x, "は100点超えちゃってますよ")
        continue
      # 以下は正しい入力が得られた時の処理
     return x

count = 5 #人数

list_score = []

sum, ave = 0, 0
# max = -1
# min = 101

for i in range(count):

    print('%i 人目の点数を入力してください ↓ '%(i+1))
    list_score.append(input_int())
    # max = math.max(max, list_score[i])
    # min = math.min(min, list_score[i])
    sum +=list_score[i]
    print() #改行してみる

print('最高点は %i , 最低点は %i, 平均値は %f ですね'%(max(list_score), min(list_score), sum/len(list_score)))


# BMIを計算します。端末から身長と体重を入力し、BMIの結果を表示します。入力が不正なときは、メッセージを表示して繰り返します。

#inputcheck.pyより
def input_float():

    while True:
     x = input("正の数値を入力してください : ")
     try:
        x = float(x)
     except ValueError:
        print(x, "は数値に変換できません")
        continue
     except:
        print("予期していないエラーです")
        exit()
     if x <=0:
        print(x, "は正の数値ではありません")
        continue
      # 以下は正しい入力が得られた時の処理
     return x

# chap5.4.pyより
def judgeBMI(bmi):
    list_strsBMI = ((0, "痩せすぎ"), (16, "痩せ"), (17, "痩せぎみ"), (18.5, "普通体重"), (25, "前肥満"), (30, "肥満(1度)"), (35, "肥満(2度)"), (40, "肥満(3度)"))
    str = ""
    for tuple in list_strsBMI:
        if tuple[0] < bmi: str=tuple[1]
        else: break
    return str

print('貴様の身長をセンチみーたーで入力しろ! ↓ ')
height = input_float()

print() #見づらいので改行してみた

print('で、体重は？ ↓ ')
weight = input_float()
print('身長%fcm、体重%fkgの場合、ぶっちゃけ「%s」だな'%(height, weight, judgeBMI(weight/((height/100)**2))))