# Cplex_dietToLoseWeight
我家猫猫好可爱

最近帮同学做作业，顺便写了点东西发上来。
具体内容是把excel中的食物信息读取下来，按照cplex规定的lp文件格式写入，调用cplex输出在约束条件下的食物搭配，从而研究其中规律，试图运用在减肥上。

总共有5个文件对应功能也很明确。
在这里简单提一下。
* main 跑起来
* readExcel 读取Excel中文件信息转化成food数组（FOOD）
* writeLp 把FOOD中信息按lp格式写入文件中
* solveByCplex 调用cplex将lp文件分析输出结果
* food 定义了food类，food类中包含营养属性。

然后就没啥了。
# 猫猫好可爱!
