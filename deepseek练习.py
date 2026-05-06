# 写一个程序，输入一个数字，输出它是“正数”、“负数”还是“零”。
num=int(input("请输入数字："))
if num>0:
    print("它是正数")
elif num==0:
    print("它是零")
else:
    print("它是负数")


# 用 for 循环计算 1 到 50 之间所有能被 3 整除的数的和，并将结果打印出来。
sum=0
for i in range(1,51):
    if i%3==0:
        sum+=i
print(sum)

# 模拟登录：
# 正确的用户名 = "test_user"，密码 = "123456"
# 用户有 3 次输入机会
# 成功则打印“登录成功”，结束程序
# 失败则提示剩余次数，3次全错打印“账户已锁定”
num=3
for i in range(3):
    name = input("请输入用户名：")
    passwd = input("请输入密码：")
    if name=="test_user" and passwd=="123456":
        print("登录成功")
        break
    else:
        num-=1
        if num > 0:
            print(f"用户名或密码错误，还剩{num}次机会")
        else:
            print("账户已锁定")

