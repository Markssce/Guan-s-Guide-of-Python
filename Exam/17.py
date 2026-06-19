import jieba
import jieba.analyse as analyse
file = open("/Users/mercury/Documents/Python/exam_data/三国演义.txt", "r", encoding='utf-8')
txt = file.read()
lists = jieba.lcut(txt)
dicts = {}
for x in lists:
    if x in dicts:
        dicts[x] = dicts[x]+1
    else:
        dicts[x] = 1
print(dicts[x])
name = input("请输入一个词： ")
while True:
    if name in dicts:
        print(dicts[name])
        break
    name = input("请输入一个词： ")

