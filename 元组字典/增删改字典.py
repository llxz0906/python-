scores={"语文":111,"数学":115,"英语":110,"政治":50,"历史":40,"地理":58,"生物":58,"音乐":92,"美术":90}
scores["化学"]=80
del scores["地理"]
scores.pop("美术")
scores["语文"]=80
print("我的化学成绩是",scores["化学"])
print("我的语文成绩是",scores["语文"])
print("我的地理成绩是",scores.get("地理"))
print("我的美术成绩是",scores.get("美术"))

