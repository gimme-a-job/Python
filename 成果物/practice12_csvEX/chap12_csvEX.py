# CSVファイルの書き込み
# カレントフォルダ（ディレクトリ）に「県人口.csv」ファイルを作成します。

import csv
import os  # 1.

prefs_out = [['東京都', 13960000],  # 2.
             ['愛知県', 7553000],
             ['大阪府', 8823000]]

with open('県人口.csv', 'w', newline='') as fout:  # 3.
    csv_out = csv.writer(fout)  # 4.
    csv_out.writerows(prefs_out)  # 5.

# csvモジュールをインポートします。
# 書き込むデータをリストのリストで準備します。
# ファイル「県人口.csv」を書き込み用にオープンします。
# with文を使用するとブロック（字下げ範囲）が終了すると、ファイルは自動で閉じられます。
# csvモジュールのwriterメソッドでCSVファイル書き込み用のwriterオブジェクトを取得します。
# writerオブジェクトのwriterowsメソッドでリストを書き込みます。


# CSVファイルの読み出し
prefs = []  # 1.
with open('県人口.csv', 'r') as fin:  # 2.
    csv_in = csv.reader(fin)  # 3.
    for row in csv_in:  # 4.
        prefs.append(row)  # 5.
    # prefs = [row for row in csv_in] # 6.
print(prefs)
# CSVファイルから読み出したデータを保存するリストを準備します。
# 「県人口.csv」ファイルを読み込み用としてオープンします。
# csvモジュールのreaderオブジェクトを取得します。
# readerオブジェクトを使用して1行ずつデータを取り出します。
# 取り出したデータをリストに追加します。
# 4～5の処理はリスト内包表記で置き換えることができます。


####################################################################################################################################################################################

# 「県人口.csv」ファイルを読み込んで、三大都市圏の人口と日本の人口に対する割合を表示してください。また、ファイルが存在しないときは、エラー「ファイルを読み込むことができません。」を表示してください。

def fileread(filename):
    list = []

    try:
        with open(filename, 'r') as fin:  # 2.
            csv_in = csv.reader(fin)  # 3.
            list = [row for row in csv_in]  # 6.

            print("Reading file " + filename + " is finished")

    except IOError:
        print("ファイルを読み込むことができません。")

    return list


population_total = 1.258*(10**8)  # "日本の人口"

list_prefs = fileread('県人口.csv')

# 参考"https://www.yoheim.net/blog.php?q=20160404"
for row in list_prefs:
    print(
        f'{row[0]}の人口は{int(row[1]):,}人、日本の総人口に対する割合は{int(row[1])/population_total*100:.3f}％です')

print(f'三大都市圏の日本の人口に占める割合は{sum([int(row[1]) for row in list_prefs])/population_total*100:.3f}％です')


###################################################################################################################################################################


# 練習問題2
# 氏名、身長と体重を入力してBMIを計算します。情報は「BMI.csv」ファイルに保存します。「end」を入力すると終了します。

# 入力例

# 名前を入力してください。東京太郎
# 身長を入力してください。200
# 体重を入力してください。150
# 東京太郎さんのBMIは37.50です。
# 終了するときは「end」を入力してください。
# 終了します。

# BMIの値を計算します。結果は小数点以下2桁表示します。

########################################################################################
# "chap5.8.py"より

# chap5.6.pyより

flg_end = False

# inputcheck.pyより


def input_float(str):

    global flg_end

    if flg_end == True:
        exit()

    while True:
        x = input(str + " : ")

        # if x == 'end':
        if checkstr_end(x):
            flg_end = True
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
          # 以下は正しい入力が得られた時の処理
        return x


def input_str(str):

    global flg_end

    if flg_end == True:
        exit()

    while True:
        x = input(str + " : ")

        # if x == 'end':
        if checkstr_end(x):
            flg_end = True
            exit()

    #  try:
    #     x = str(x)

    #  except:
    #     print("予期していないエラーです")
    #     exit()

          # 以下は正しい入力が得られた時の処理
        return x

# chap5.4.pyより


def judgeBMI(bmi):
    list_strsBMI = ((0, "痩せすぎ"), (16, "痩せ"), (17, "痩せぎみ"), (18.5, "普通体重"),
                    (25, "前肥満"), (30, "肥満(1度)"), (35, "肥満(2度)"), (40, "肥満(3度)"))
    str = ""
    for tuple in list_strsBMI:
        if tuple[0] < bmi:
            str = tuple[1]
        else:
            break
    return str


def checkstr_end(str):
    list_str = ('end', 'End', 'END')

    for tuple in list_str:
        if str == tuple:
            return True
            exit()  # "要る？"

    return False


# while flg_end != True:

#     name = input_str('名前を入力してください。')

#     height = input_float('身長を入力してください。')

#     weight = input_float('体重を入力してください。')

#     val_bmi = weight/((height/100)**2)

#     print(f'{name}さんのBMIは{val_bmi:.2f}です。')

# 以上"chao5.8.py"より
#########################################################################################################################################

# おまけ
# プログラムを起動したときにファイルが存在するときは、次のメッセージを表示します

# 「ファイルが存在します。上書きするときは1を、追加するときは2を、プログラムを終了するときは0を入力してください。」

# 入力された数字の動作を行います。ファイルの存在を確認する方法は調べてください。


def input_int(str, min, max):

    global flg_end

    if flg_end == True:
        exit()

    while True:
        x = input(str + " : ")

        # if x == 'end':
        if checkstr_end(x):
            flg_end = True
            exit()

        try:
            x = int(x)
        except ValueError:
            print(x, "は数値に変換できません")
            continue
        except:
            print("予期していないエラーです")
            exit()
        if x < 0:
            print(x, "は正の数値ではありません")
            continue
        if x<min or max<x:
            print(f'{min}から{max}までの整数で入力してください')
            continue

          # 以下は正しい入力が得られた時の処理
        return x

flg_end = False

filename = input_str('ファイル名を入力してください')

answer = -1

# 参考"https://python.keicode.com/lang/file-exists.php"より
if os.path.isfile(filename): answer=input_int('ファイルが存在します。上書きするときは1を、追加するときは2を、プログラムを終了するときは0を入力してください。', 0, 2)

print(f'{answer}の処理を開始します')