# 5.8 数値を表示する際のフォーマット指定

# BMIの値を計算します。結果は小数点以下2桁表示します。
#chap5.6.pyより

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

val_bmi = weight/((height/100)**2)

# 参考"https://magazine.techacademy.jp/magazine/23378"
print('身長%.1fcm、体重%.1fkgの場合、BMI値は%.2fであるからぶっちゃけ「%s」だな'%(height, weight, val_bmi, judgeBMI(val_bmi)))

# Pythonには情報を表示する方法が複数あります。調査してください。