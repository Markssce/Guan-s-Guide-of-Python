import matplotlib.pyplot as plt # Error
plt.rcParams['font.sans-serif']=['Arial Unicode MS']
fig = plt.figure(figsize=(12,9))
fig.add_subplot(121)
option=["宣传不到位","环保意识不强","收集站分布不合理","投放时间不方便","乱扔垃圾未处罚","管理不到位"]
data=[17,44,17,41,24,19]

plt.bar(range(6),data) # Error
plt.title("小区垃圾分类还存在的问题")
plt.xticks(range(6), option, rotation=45)# Error
plt.xlabel("选项")
plt.ylabel("回复情况")
fig.add_subplot(122)
plt.pie(data, labels=option,autopct='%4.1f%%')# Error
plt.show()