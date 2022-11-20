# 5.3 while文による繰り返し

# 5回繰り返す処理を記述記述してください。繰り返し回数を表示してください。
from webbrowser import get


count = 0
while (count < 5):
    print("今は %i 回目の繰り返しです。"%(count+1))
    count +=1

# 1～100までの合計を求めてください。

def getSum(list):
    i = 0
    sum = 0
    while (i < len(list)):
        sum += list[i]
        i+=1
    return sum

nums = list(range(1, 100+1))
# i = 0
# sum = 0
# while (i < len(nums)):
#     sum += nums[i]
#     i+=1

sum = getSum(nums)

print(sum)

# リストのデータを表示してください。リストには添え字を使用してアクセスしてください。
j = 0
while (j < len(nums)):
    if (j+1)%10 != 0: print(nums[j], end=", ")
    else:print(nums[j])
    j+=1

# リスト ['Fukuoka', 'Kumamoto', 'Kagoshima'] のデータを表示してください。リストには添え字を使用してアクセスしてください。
list_pref = ['Fukuoka', 'Kumamoto', 'Kagoshima']
k=0
while(k< len(list_pref)):
    print(list_pref[k])
    k+=1

# リストの合計値、平均値を表示してください。
# print('リストの合計値は %i で、平均値は %f です。'%(sum, sum/len(nums)))

def show_sum_ave(list):
    # リストの合計値、平均値を表示してください。
    sum = getSum(list)
    print('リストの合計値は %i で、平均値は %f です。'%(sum, sum/len(list)))

show_sum_ave(nums)

# リスト [5, 7, 1, 3, 8] の合計値、平均値を表示してください。

list57138 = [5, 7, 1, 3, 8]
show_sum_ave(list57138)

