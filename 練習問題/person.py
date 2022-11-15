class Person():
    """個人の体重管理を行います。"""

    def __init__(self, first_name, last_name, age, height, weight):
        """インスタンス変数を初期化します。"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight

    def bmi(self):
        """BMIを計算します。"""
        return self.weight/(self.height/100*self.height/100)

    def info(self):
        """BMIの結果の情報を表示します。"""
        bmi = self.bmi() # すでに定義されたメソッドを利用します。
        if bmi < 18.5:
            print('低体重です。')
        elif bmi < 25:
            print('普通体重です。')
        elif bmi < 30:
            print('肥満（1度）')
        elif bmi < 35:
            print('肥満（2度）')
        elif bmi < 40:
            print('肥満（3度）')
        elif bmi >= 40:
            print('肥満（4度）')


if __name__ == '__main__': # エントリーポイント
    # このファイルがモジュールとして読み込まれたときは実行されません。
    person = Person(first_name='Taro', last_name='Tokyo', age=50, height=170, weight=60)
    # person = Person(age=50, height=170, weight=60, first_name='Taro', last_name='Tokyo')
    # person = Person('Taro', 'Tokyo', 50, 170, 60)
    bmi = person.bmi()
    print(f'{person.last_name} {person.first_name} さんのBMIは {person.bmi():.2F}です。')
    person.info()
