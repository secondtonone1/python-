#-*-coding:utf-8-*-
infos = {"李明":23, "豆豆":22,"老李":55}
print("李明的年龄为%d" %(infos["李明"]))
infos["王立冬"]=32
print (infos)
#print (infos["梁田"])
if not ("梁田" in infos):
	print("梁田不在记录")
print(infos.get("梁田"))
print(infos.get("梁田","梁田不在记录"))
infos.pop("王立冬")
print (infos)