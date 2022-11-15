# 練習2
# with open('bmi.csv', 'r') as f:
#     data = f.read() # まとめて読みだす
#     data = data.split() # 改行で区切る

#     print(data) # デバッグ用

#     # 画面出力
#     for d in data: # 1つ目のリストを取得
#         # print(d)
#         d = d.split(',') # カンマで切り出したリスト
#         for x in d: # リストの各項目を1つずつ出力
#             print(x + ' ', end='') # 改行なし
#         print() # 1行分のデータを出力したら改行

# 練習1
## データ構造をどうする？
data = [['東京太郎', 200, 150],
        ['名古屋次郎', 150, 100],
        ['大阪三郎', 180, 130]]

with open('bmi.csv', 'w') as f:
    for row in data: # 1つ目のリストを取得
        for col in row: # 出力する項目を取得
            # 項目を書き出し(str型しか書き込みできません)
            f.write(str(col)) # 数値はstr型に変換
            f.write(',')
        f.write('\n') #　改行を出力

# with open('bmi.csv', 'w') as f:
#     for row in data:
#         for i in range(len(row)): # データ数分だけ繰り返し
#             f.write(str(row[i]))
#             if i != len(row)-1: # 最後のデータでなければ
#                 f.write(',')
#         f.write('\n')

