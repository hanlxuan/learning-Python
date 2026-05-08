# # 写一个程序，输入一个数字，输出它是“正数”、“负数”还是“零”。
# num=int(input("请输入数字："))
# if num>0:
#     print("它是正数")
# elif num==0:
#     print("它是零")
# else:
#     print("它是负数")
#
#
# # 用 for 循环计算 1 到 50 之间所有能被 3 整除的数的和，并将结果打印出来。
# sum=0
# for i in range(1,51):
#     if i%3==0:
#         sum+=i
# print(sum)
#
# # 模拟登录：
# # 正确的用户名 = "test_user"，密码 = "123456"
# # 用户有 3 次输入机会
# # 成功则打印“登录成功”，结束程序
# # 失败则提示剩余次数，3次全错打印“账户已锁定”
# num=3
# for i in range(3):
#     name = input("请输入用户名：")
#     passwd = input("请输入密码：")
#     if name=="test_user" and passwd=="123456":
#         print("登录成功")
#         break
#     else:
#         num-=1
#         if num > 0:
#             print(f"用户名或密码错误，还剩{num}次机会")
#         else:
#             print("账户已锁定")

# 5.8日
# 给定列表 nums = [3, 8, 2, 10, 5]，用两种方法求最大值：
# nums = [3, 8, 2, 10, 5]
# # 方法1：用 max() 函数
# print(max(nums))
# # 方法2：用 for 循环自己找最大值
# max=0
# for i in nums:
#     if i>max:
#         max=i
# print(max)

# 题目1：列表求和
# 给定 lst = [4, 7, 2, 9, 1]，用 for 循环计算所有元素的和，打印结果。
lst = [4, 7, 2, 9, 1]
sum=0
for i in lst:
    sum+=i
print(sum)
# 题目2：偶数筛选
# 给定 lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，用 for 循环和 if，把所有偶数放入一个新列表 even_lst，最后打印 even_lst。
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list=[]
for i in lst:
    if i%2==0:
        even_list.append(i)
print(even_list)
# 题目3：打印乘法表的一行
# 输入一个数字 n（比如 5），打印 1*n, 2*n, ..., 10*n 的结果，用 for 循环。
# 例如 n=3，输出：3 6 9 12 15 18 21 24 27 30
num=int(input("请输入："))
for i in range(1,num+1):
    sum=i*num
    print(sum)
# 题目4：字符串反转
# 输入一个字符串 s = "Python"，用 for 循环反转它，输出 "nohtyP"。（提示：可以新建空字符串，逐个字符拼接）
s = "Python"
reversed_s = ""
for ch in s:
    reversed_s = ch + reversed_s   # 每次把新字符加到前面
print(reversed_s)
# 题目5：统计列表中某个值的出现次数
# 给定 lst = [1, 3, 5, 3, 2, 3, 4]，统计数字 3 出现了几次，打印结果。
lst = [1, 3, 5, 3, 2, 3, 4]
print(lst.count(3))