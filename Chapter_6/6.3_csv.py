fp = open("/Users/mercury/Documents/Python/exam_data/Data.csv", "r", encoding="gbk")
lines = fp.readlines()
fp.close()

data = []
for i in lines[1:]:
    i = i.strip() # 去掉换行符
    grow_data = i.split(',')
    data.append(int(grow_data[2]))
max_ = max(data)
min_ = min(data)
aver_ = sum(data)/len(data)
print("最高成长值：%d\n最低成长值：%d\n平均成长值：%4.1f"%(max_, min_, aver_))
fp = open("/Users/mercury/Documents/Python/exam_data/New_Data.csv", "w", encoding="gbk")

lis_w = ["最高成长值,最低成长值,平均成长值\n","%s,%s,%s"%(str(max_), str(min_), str(aver_))]
# write:
for i in range(2):
    fp.write(lis_w[i])

# writelines:
# fp.writelines(lis_w)
fp.close()
