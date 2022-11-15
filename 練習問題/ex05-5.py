# 5.5
# ans = 25 # 回答

# count = 0 # 失敗した回数
# while True:
#     # データ入力
#     while True:
#         data = int(input('データを入力してください：'))
#         if data < 1 or data > 50:
#             print('正しいデータを入力してください。')
#             continue
#         break

#     count += 1
#     if data == ans:
#         print('正解です。')
#         break
#     elif data < ans:
#         print("小さいです")
#     else:
#         print("大きいです")
    
# # 終了する前に回数を表示
# print(str(count) + "回で正解しました。")

scores = [] # 人数分の点数を入力するリスト
# for i in range(5):
count = 0 # 正しいデータが入力された回数
while True: # 無限ループ
    score = input("点数を入力してください。") # データを入力
    score = int(score) # 文字列を整数に変換
    
    # TODO: データのチェック（検証：Validation）
    if score < 0 or score > 100:
        print('正しい点数を入力してください。')
        continue # ループの先頭に戻る
    
    count += 1 # 正しい値が入力された回数を+1
    if count > 5: # 5回入力されたら終了
        break

    scores.append(score)
    # print(score, type(score))

# TODO: 最高点、最低点、平均を求める

print(scores)