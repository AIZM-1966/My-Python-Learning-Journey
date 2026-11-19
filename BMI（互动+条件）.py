user_weight = float(input('请输入您的体重(单位：kg)'))
user_height = float(input('请输入您的身高(单位：m)'))
user_BMI = user_weight / (user_height)**2
print('您的BMI指数是'+str(user_BMI))
if 18.5 <= user_BMI <= 25:
    print('您的人体胖瘦程度属于正常水平，请继续保持！坚持健康生活。')
elif user_BMI<18.5:
    print('您的人体胖瘦程度属于消瘦水平，请增加饮食摄入！避免营养不良。')
elif 25 < user_BMI <= 30:
    print('您的人体胖瘦程度属于偏胖水平，请控制饮食摄入！避免疾病发生。')
else:
    print('您的人体胖瘦程度属于肥胖水平，请严格控制饮食摄入！防止心脑血管疾病发生！')