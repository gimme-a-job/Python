import math

# 第3章　変数と演算、代入の練習問題

# データ型の表示（typeof使用）
# 変数に格納されているデータの型を予想してください。結果をプログラムで確認してください。

a = 1
b = 1.0
c = 10/2
d = 10//2
e = '1'
f = "1.0"
print(type(a), type(b), type(c), type(d), type(e), type(f))

# 複数変数への代入
# Pythonでは複数変数への代入（代入の=の左右に複数変数の記述）が可能です。 次のプログラムは変数aとbの値を入れ替えますが、複数変数の機能を使用せずに同じ機能を実現する方法を考えてください。
a = 'Tokyo'
b = 'Osaka'
a, b = b, a
print(a, b)

tmp =a
a =b
b =tmp
print(a,b)

# 三角形の面積を計算するプログラム
# 底辺が10、高さが5の三角形の面積を求めてください。
bottom = 10
height = 5
area = bottom * height /2
print(area)

# 消費税の計算を行うプログラム
# 5万円のパソコン1台、2万円のモニタ1台、2000円のマウス1台、1000円のマウスパッドを1枚購入しました。合計金額（税込）と消費税を表示してください。

def showTax(price):
    tax = math.ceil(price * 0.1) #～銭は店側負担だった気がするので今回は切り捨て
    # print("合計金額（税込）:" + '(price+tax)' + ", 消費税:" + 'tax') #これだとエラー
    print("合計金額（税込）: %i , 消費税: %i"%( (price+tax), tax ))

sum = 50000 + 20000 + 2000 + 1000
showTax(sum)

# BMIを計算するプログラム
# 肥満度を表す指標としてBMIがあります。BMIの計算式を調べて身長170cm、体重70kgの人間のBMI値を求めてください。
h = 170 / 100
w = 70

def getBMI(height, weight):
    return weight / (height * height)

print(getBMI(h,w))

# 複利計算
# 元金、利息率、期間（年単位）を入力すると最終段階の金額を計算するプログラムを作成してください。
# 計算式 a: 元金、元本、初期段階で持っている金額、現在価値（PV: Present Value） r: 利息率、年利率、運用利率、利回り n: 期間、運用期間 b: 最終段階の金額、将来価値（FV: Future Value）
pv = float(input("元金、元本、初期段階で持っている金額、現在価値（PV: Present Value） : "))
r = float(input("利息率、年利率、運用利率、利回り : "))
n = float(input("期間、運用期間 : "))
fv = pv * ((1+r)**n)
print("最終段階の金額、将来価値（FV: Future Value） : %f"%fv)

# n乗根を求める（応用）
# テキスト2の「2 コラム ニュートン法」を確認して、n乗根を求めるプログラムを作成してください。

# p102_5-17.pyより

# "inputcheck.py"より
while True:
    x = input("正の数値を入力してください ")

    if x == "end":  # 「５」のために追加
        exit()

    try:
        x = float(x)
    except ValueError:
        print(x, "は数値に変換できません")
        continue
    except:
        print("予期していないエラーです")
        exit()
    if x <= 0:
        print(x, "は正の数値ではありません")
        continue

    # n_temp = input(x,"の何乗根を求めますか ")
    n_temp = input("%fの何乗根を求めますか "%x)

    if n_temp == "end":  # 「５」のために追加
        exit()

    try:
        n_temp = float(n_temp)
    except ValueError:
        print(n_temp, "は数値に変換できません")
        continue
    except:
        print("予期していないエラーです")
        exit()
    if n_temp <= 0:
        print(n_temp, "は正の数値ではありません")
        continue



# 以下は正しい入力が得られた時の処理

    # x の平方根を求める
    
    #
    
    rnew = x
    n_new = n_temp
    
    #
    
    # diff = rnew - x/rnew #abs()を使わない場合
    # if diff < 0:
    #     diff = -diff
    
    # diff = abs(rnew - x/rnew) #abs()を使う場合
    r1 = (n_new-1)*rnew
    r2 = x/((rnew)**(n_new-1))
    diff = abs( (r1 - r2) /rnew ) #abs()を使った相対精度になってるといいが⇒なってるっぽい？
    
    # while (diff > 1.0E-6):
    while (diff > 1.0E-10):
        
        # r1 = rnew
        r1 = (n_new-1)*rnew
        
        # r2 = x/r1
        r2 = x/((rnew)**(n_new-1))
        
        # rnew = (r1 + r2)/2
        rnew = (r1 + r2)/n_new

        print(r1, rnew, r2)
        
        # diff = r1 - r2
        # if diff < 0:
        #     diff = -diff
        
        # diff = abs(r1 - r2) #abs()を使った絶対精度？

        diff = abs( (r1 - r2) /rnew ) #abs()を使った相対精度になってるといいが⇒なってるっぽい？

# 04-Oct-22 上手くいかないが諦めた
