# 4.8 リストへの追加、結合
# 1から9の要素を持つリストの最後に10を追加してください。
list1 = list(range(1,9+1))
list1.append(10)
print(list1) #検証用に追加

# 空のリストを作成し、後から'Tokyo'、'Kanagawa'と'Saitama'を追加してください。
list2 = []
list2.append('Tokyo')
list2.append('Kanagawa')
list2.append('Saitama')
print(list2) #検証用に追加

# 1から5までの要素を持つリストlist_firstと、6から10までの要素を持つlist_secondを作成し、2つのリストを結合したリストlist_allを作成してください。
list_first = list(range(1, 5+1))
list_second = list(range(6, 10+1))

# list_all = list_first.extend(list_second)
list_temp = list_first.copy()
list_temp.extend(list_second)
list_all = list_temp

print(list_first) #検証用に追加
print(list_second) #検証用に追加
print(list_all) #検証用に追加

# （応用）リストはPythonで重要な機能です。インターネットなどで調査して、次のプログラムを作成してください。
# リスト[1, 3, 5]の1と3の間に2を、3と5の間に4を追加してください。insert関数を使用してください。


# [0, 1, 1, 2, 3, 4, 5]から重複した1を削除してください。delを使用してください。

# ['Tokyo', 'Osaka', 'Nagoya', 'Fukuoka']から'fukuoka'を削除します。remove関数を使用してください。

# ['Tokyo', 'Osaka', 'Nagoya', 'Fukuoka']の中で、'Osaka'の要素がある要素番号を取得してください。index関数を使用してください。

# ['Kagawa', 'Ehime', 'Tokushima', 'Kochi']に'Ehime'が含まれているか確認します。inを使用してください。

# [0, 1, 1, 2, 3, 4, 5]に1と3と6が含まれている個数を表示します。count関数を使用してください。

# [7, 1, 3, 6, 5]を昇順と降順に並べ替えてください。sort関数を使用してください。