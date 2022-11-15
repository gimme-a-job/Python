# 第11章 クラス
# Personクラスを作成して動作を確認します。属性は、氏名（姓と名）、年齢、身長と体重とします。
# PersonクラスにBMIを計算するbmiメソッド、情報を表示するinfoメソッドを追加してください。infoメソッドは肥満度によってコメント（例　普通体重です。）を付けてください。

# 計算結果はkeisanで確認しましょう。

class Person:
    
    def __init__(self, first_name, last_name, age, height, weight)  -> None:
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.height=height
        self.weight=weight
        # self.bmi=self.bmi()
    
    def bmi(self):
        return self.weight/((self.height/100)**2)

    def info(self):
        # bmi = self.bmi(self) #これだと動かない
        
        #パターン１
        # bmi = self.bmi()
        # return self.judgeBMI(bmi)

        #パターン２
        # return self.judgeBMI(self.bmi)

        #パターン３
        return self.judgeBMI()

    # chap5.4.pyより
    # def judgeBMI(bmi): #これだと動かない
    # def judgeBMI(self, bmi):
    def judgeBMI(self):
        bmi = self.bmi()
        list_strsBMI = ((0, "痩せすぎ"), (16, "痩せ"), (17, "痩せぎみ"), (18.5, "普通体重"), (25, "前肥満"), (30, "肥満(1度)"), (35, "肥満(2度)"), (40, "肥満(3度)"))
        str = ""
        for tuple in list_strsBMI:
          if tuple[0] < bmi: str=tuple[1]
          else: break
        return print(str)

    def showBMI(self):
        print(f'{self.last_name} {self.first_name} さんのBMIは{self.bmi()}です')



person = Person(first_name='Taro', last_name='Tokyo', age=50, height=170, weight=60)
bmi = person.bmi()
print(f'{person.last_name} {person.first_name} さんのBMIは{person.bmi()}です')

person.info()



# 3人分のPersonインスタンスを作成して、最後にBMIの一覧、体重と身長の平均を表示してください。データはキーボードから入力します。

# 東京太郎さんのBMIは〇〇です。
taro_tokyo = Person(first_name='太郎', last_name='東京', age=50, height=170, weight=60)
taro_tokyo.showBMI()
taro_tokyo.info()

# 大阪次郎さんのBMIは〇〇です。
jiro_osaka = Person(first_name='次郎', last_name='大阪', age=5, height=17, weight=6)
jiro_osaka.showBMI()
jiro_osaka.info()

# 名古屋三郎さんのBMIは〇〇です。
saburo_nagoya = Person(first_name='三郎', last_name='名古屋', age=500, height=1700, weight=600)
saburo_nagoya.showBMI()
saburo_nagoya.info()

# 体重の平均は〇〇、身長の平均は〇〇です。
list_people = [taro_tokyo, jiro_osaka, saburo_nagoya]
sum_height, min_height, max_height = sum([p.height for p in list_people]), min([p.height for p in list_people]), max([p.height for p in list_people])
sum_weight, min_weight, max_weight = sum([p.weight for p in list_people]), min([p.weight for p in list_people]), max([p.weight for p in list_people])

print(f'体重の平均は{sum_weight/len(list_people)}、身長の平均は{sum_height/len(list_people)}です')

# 😵😵😵複数名のPersonオブジェクトをリストで管理します。身長と体重の平均、最小と最大を求めてください。
print(f'身長の最小は{min_height}、最大は{max_height}です')
print(f'体重の最小は{min_weight}、最大は{max_weight}です')