# -*- coding:utf-8 -*-
import json
# 修改以下名字为从成绩分析报告里下载的xlsx文件转换成的csv文件名
class_name = "阶段考试分析报告-2019-02-14"
# 打开分组信息json文件
f1 = open("ceshi9.json")
names = json.load(f1)
# print(names)
# print(data['1'])
f1.close()
# 打开班级成绩表
f2 = open("%s.csv" % class_name)
# 处理成绩表，获取每个人的姓名和成绩
source_scores = f2.readlines()
f2.close()
temp_scores = [i.strip() for i in source_scores]
scores = [i.split(',') for i in temp_scores[4:]]
print(scores)
# 定义一个空字典来存放处理后的小组成绩
group_scores = {}
for i in range(1,13):
    # 定义一个空列表，存放每个小组的成绩，然后添加到group_scores字典里
    alist = []
    for _ in scores:
        if _[1] in names[str(i)]:
            if _[-1] != '未交卷':
                alist.append(_[-1])
    # 打印各组每人的成绩
    # print("%02d" % i,alist)
    # print("%02d" % i,names[str(i)])
    group_scores[i] = alist
# 创建一个csv文件，将小组，平均分和组员写入csv文件
f3 = open("%s_avg.csv" % class_name ,'w',encoding='gbk')
f3.write("小组,平均分,小组人数,组员姓名\n")
nums_total = 0
for n,v in group_scores.items():
    v = [float(i) for i in v]
    # 计算平均分
    avg = round(sum(v)/len(v),2)
    nums = len(names[str(n)])
    print( "%02d" % n, "%.2f" % avg,"%s人" % nums,names[str(n)])
    # 将小组序号、平均分、小组人数和组员姓名写入csv文件
    f3.write("%02d" % n)
    f3.write(",")
    f3.write("%.2f" % avg)
    f3.write(",")
    f3.write("%s人" % nums)
    f3.write(",")
    # 写入csv文件
    for name in names[str(n)]:
        f3.write(name)
        f3.write(",")
    f3.write("\n")
    nums_total += nums
f3.close()
print("共%s人" % nums_total )

