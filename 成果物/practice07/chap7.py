import math

# 第7章 関数を使った処理のカプセル化


# 引き数で渡されたリストの合計を返却するsum_list関数を作成してください。
def sum_list(data):

    sum = 0
    for d in data:
        sum += d

    return sum


sum = sum_list([1, 2, 3, 4, 5])
print(sum)


# 引き数で渡された身長と体重からBMIを計算して返却するcalc_bmi関数を作成してください。BMI値を受け取り、該当するメッセージを表示するbmi_print関数も作成してください。
def calc_bmi(height, weight):
    return weight/((height/100)**2)


def print_bmi(bmi):
    # chap5.4.pyより
    list_strsBMI = ((0, "痩せすぎ"), (16, "痩せ"), (17, "痩せぎみ"), (18.5, "普通体重"),
                    (25, "前肥満"), (30, "肥満(1度)"), (35, "肥満(2度)"), (40, "肥満(3度)"))
    str = ""
    for tuple in list_strsBMI:
        if tuple[0] < bmi:
            str = tuple[1]
        else:
            break
    print(str)


bmi = calc_bmi(170, 80)
print_bmi(bmi)


# 引き数で渡されたリストの値を2倍にするdouble_list関数を作成してください。
def double_list(data):
    return [2*i for i in data]

print(double_list([1, 2, 3, 4, 5]))


# 面積を求めるget_area関数を作成してください。引き数に、実際の面積を計算する関数オブジェクトと、計算に必要なデータを渡します。

#我が想定した問題
# def get_area(data):
#     return data[1](data[0]['bottom'], data[0]['height'])


# def triangle(bottom, height):
#     return bottom*height/2


# print(get_area([{'bottom': 100, 'height': 150}, triangle]))

#実際の問題
def get_area(data, f):
    
    if len(data) == 1: #もっとユニークに判定できないものか
        # return f(data[0]) #添え字呼び出し不可
        return f(data['radius'])
    if len(data) == 2: #もっとユニークに判定できないものか
        # return f(data[0], data[1]) #添え字呼び出し不可
        return f(data['bottom'], data['height'])

def triangle(bottom, height):
    return bottom*height/2


print(get_area({'bottom': 100, 'height': 150}, triangle))



# 先ほどのプログラムで、円の面積も求められるように修正してください。

def circle(radius):
    return (radius**2)*math.pi

print(get_area({'radius': 50} , circle))



# 🤔引き数で渡されたリストの要素を表示するprint_list関数を作成してください。リストの中に含まれるリストの値も表示します。ネストは1レベルとします。（いわゆるフラット化）
def print_list(data):
    for d in data:
        
        #動かない
        # if len(d) > 1: print_list(d)
        # else: print(d, end=', ')

        #動くがintのリスト以外動かないだろう
        # if type(d) is int: print(d, end=', ')
        # else: print_list(d)

        if type(d) is list: print_list(d)
        else: print(d, end=', ')
        


print_list([1, 2, [3, 4, 5], 6, 7, [8, 9], 10])

print() #改行死体

print_list([1, 2, [3, [4, 5]], 6, 7, [8, 9], 10])

print() #改行死体

# print(type([1, 2, 3])) #検証用

print_list([1, [2, [3, [4, 5, [6, [7, [8, [9, [10] ] ] ] ] ] ] ] ]  )

print() #改行死体

print_list([ 'はまの', ['fx', ['大好き'] ] , [1, [2, [3, [4, 5, [6, [7, [8, [9, [10, ['ホアン', ['ツォン', ['ラン'] ] ] ] ] ] ] ] ] ] ] ]]  )

# 🤔🤔🤔先ほどのプログラムを修正して、ネストのレベルの制限をなくしてください。 ヒント：再帰処理を使用します。
