import jieba
# Simplified Mode
lst =jieba.lcut('小郭老师本科毕业于同济大学，后在耶鲁大学深造')
print(lst)

# cut_all Mode
lst =jieba.lcut('小郭老师本科毕业于同济大学，后在耶鲁大学深造', cut_all = True)
print(lst)

# Search Engine Mode
lst=jieba.lcut_for_search('小郭老师本科毕业于同济大学，后在耶鲁大学深造')
print(lst)

##
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