fp = open("/Users/mercury/Documents/Python/Chapter_6/6_2.txt", "w")
lines = ["竹外桃花三两枝，", "春江水暖鸭先知。", "蒌蒿满地芦芽短，", "正是河豚欲上时。"]
for line in lines:
    fp.write(line + '\n')

# lines=["竹外桃花三两枝，\n","春江水暖鸭先知。\n","蒌蒿满地芦芽短，\n","正是河豚欲上时。\n"]
# fp.writelines(lines)

fp.close()