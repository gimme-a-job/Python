## 7
#
# def sum_list(data):
#     sum = 0
#     for d in data:
#         sum += d
#     return sum
#     # return sum(data)

# sum = sum_list([1, 2, 3, 4, 5])
# print(sum)

# def calc_bmi(height, weight):
#     return weight / (height/100 * height/100)

# def print_bmi(bmi):
#     if bmi < 18.5:
#         print('低体重')
#     elif bmi < 25:
#         print('普通体重')
#     elif bmi < 30:
#         print('肥満（1度）')
#     elif bmi < 35:
#         print('肥満（2度）')
#     elif bmi < 40:
#         print('肥満（3度）')
#     else:
#         print('肥満（4度）')

# bmi = calc_bmi(170, 80)
# print_bmi(bmi)

#
# def double_list(data):
#     for i in range(len(data)):
#         data[i] *= 2
#     return data
#     # return [ x * 2 for x in data]

# print(double_list([1, 2, 3, 4, 5]))

#
def get_area(data, f):
    return f(data["bottom"], data["height"])

def triangle(bottom, height):
    return bottom * height / 2

print(get_area({'bottom': 100, 'height': 150}, triangle))

#
def get_area(data, f):
    return f(data["radius"])

def circle(radius):
    return 3.14 * radius * radius

print(get_area({'radius': 100}, circle))