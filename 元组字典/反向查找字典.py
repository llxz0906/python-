scores={"语文":111,"数学":115,"英语":110,"政治":50,"历史":40,"地理":58,"生物":58,"音乐":92,"美术":90}
scores_kemu={}
for kemu,fen in scores.items():
    scores_kemu[fen]=kemu
print("115分的科目为",scores_kemu[115])

