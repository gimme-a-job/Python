import math

# 5.7 Pythonでの数学関数

# 半径を入力し、円の面積と円周を表示してください。円周率は数学ライブラリを使用してください。

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

def getArea(radius):
    return math.pi*(radius**2)

def getCircumference(radius):
    return 2*math.pi*radius

print('半径を入力してください')
radius = input_float()

print('半径 %f の円の面積は %f 、円周は %f です。'%(radius, getArea(radius), getCircumference(radius)))


# 半径のリスト（例 [1, 2, 3, 4, 5]）が与えられたとき、各半径の円の面積を求めてリストに保存してください。
list_radius = [1, 2, 3, 4, 5]
list_areas = [getArea(i) for i in list_radius]
print(list_radius) #検証用に追加
print(list_areas) #検証用に追加


# リストの最大値と最小値を求めてください。数学ライブラリを使用してください。
print('円の面積の最大値は %f 、最小値は %f です。'%(max(list_areas), min(list_areas)))
