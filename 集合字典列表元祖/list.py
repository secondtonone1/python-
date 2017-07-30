#-*-coding:utf-8-*-
animals = ["大象","猴子","蚂蚁","豪猪"]
print ("动物园有这些动物:", animals)
lion = "狮子"
print ("新来了", lion)
animals.insert(1,lion)
print ("动物园有这些动物:", animals)
animals.pop(3)
print ("蚂蚁灭绝了")
print ("动物园有这些动物:", animals)
print ("老虎和狮子交配生了两个小宝宝")
babies = ["小宝宝1号", "小宝宝2号"]
animals.insert(2,babies);
print ("动物园有这些动物:", animals)
print("饲养员给两个小宝宝取了名字")
animals[2][0]="小毛"
animals[2][1]="大毛"
print ("动物园有这些动物:",animals)
print("列表中有%d个元素"  %len(animals))
print("第三个元素包含%d个元素" %len(animals[2]))