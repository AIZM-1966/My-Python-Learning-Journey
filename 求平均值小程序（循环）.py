print('这是一个求平均值的小程序')
total=0
count=0
user_input = input('请输入数字（当所有数字输入完后，请输入q来终止程序）：')
while user_input !='q':
    number = float(user_input)
    total += number
    count += 1
    user_input = input('请输入数字（当所有数字输入完后，请输入q来终止程序）：')
if count == 0:
    print('你没有输入任何数字，无法计算平均值！')
else:
    result = total / count
    print('您所求的平均值为：'+ str(result))