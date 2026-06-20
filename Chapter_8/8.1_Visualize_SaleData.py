import matplotlib.pyplot as plt
plt.figure(figsize = (6, 4))
plt.rcParams['font.sans-serif']= ['SimHe']

seasons = ["Season_1", "Season_2", "Season_3", "Season_4"]
sales = [2780, 1950, 2680, 2120]
index = [0, 1, 2, 3]
barW = 0.7

plt.title("Sales")
plt.xlabel("Time")
plt.ylabel("Sales volume")
plt.xticks(index, seasons)
plt.grid(axis = 'y')

plt.bar(index, sales, barW, color = 'r', label = "Product_1")
for a, b in zip(index, sales):
    plt.text(a, b+30, '%.0f'%b, ha = 'center', fontsize = 9)

plt.legend(loc='upper right')
plt.show()