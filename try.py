# -*- coding:utf-8 -*-
import time
# start1 = time.time()
# for i in range(100000):
#     print('hello')
# end1 = time.time()
# print(end1-start1)
#
# start2 = time.time()
# i = 0
# while i < 100000:
#     print('hello')
#     i += 1
# end2 = time.time()
# print(end2-start2)
# print(end1-start1)

# i = 1
# n = int(input("请输入一个整数："))
# while i < n:
#     print(('*' * (2*i - 1)).center(2*n - 1))
#     # print(' ' * (n -i) + '*'*(2*i - 1) )
#     i += 1
# print('    *')
# print('   ***')
# print('  *****')
# print(' *******')
# print('*********')


# for i in range(100):
#     if i % 2 == 0 and i % 5 == 0:
#         print(i)
#
# # 遍历100-200
# # 然后遍历2-i，让i除以这个数，判断时候余数为0
# for i in range(100,200):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#         else:
#             print(i)
#             break








# i = 0
# while i < 5:
#     print('hello')
#     i += 1

# sum = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         sum += i
# print(sum)


# 求一个数（1-100），既能被2整除也能被5整除

# - 判断101-200之间有多少个素数，并输出所有素数。

#素数：这个数除以1余数=0，除以它本身余数也是0，除以1到它本身之间的数余数都不为0

# 遍历100-200，变量为i

# 判断i除以2到i之间的整数，余数是否为0，只要出现为0的，这个数就不是素数

# 13

# for i in range(100,201):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     # 如果循环正常结束，就会执行else里的代码；如果是break循环终止，就不执行else里的代码
#     else:
#         print(i)

# for i in range(5):
#     # if i == 1:
#     #     break
#     print(i)
# else:
#     print('hello')



# 求一个数（1-100），既能被2整除也能被5整除

# - 判断101-200之间有多少个素数，并输出所有素数。

#素数：这个数除以1余数=0，除以它本身余数也是0，除以1到它本身之间的数余数都不为0

# 遍历100-200，变量为i

# 判断i除以2到i之间的整数，余数是否为0，只要出现为0的，这个数就不是素数

# i = 101
# n = 0
# while i <= 200:
#     j = 2
#     while j < i:
#         if i % j == 0:
#             break
#         j += 1
#     else:
#         n += 1
#         print(i)
#     i += 1
# print(n)


# 求一个数（1-100），既能被2整除也能被5整除

# - 判断101-200之间有多少个素数，并输出所有素数。

#素数：这个数除以1余数=0，除以它本身余数也是0，除以1到它本身之间的数余数都不为0

# 遍历100-200，变量为i

# 判断i除以2到i之间的整数，余数是否为0，只要出现为0的，这个数就不是素数

# i = 101
# n = 0
# while i <= 200:
#     j = 2
#     # k = 0
#     while j < i: # 6/2 k = 1 ;6/3 k =2 ;6/4 k =2;6/5 k=2
#         if i % j == 0:
#             print("%d不是素数" % i)
#             # k += 1
#             break
#         j += 1
#     else:
#         n += 1
#         print("%d是素数"%i)
#
#     i += 1
# print("素数有%d个"%n)

import xlrd

file_name = "阶段考试分析报告-2019-01-21.xls"
data = xlrd.open_workbook(file_name)
table = data.sheets()[0]
names = table.col_values(1)
scores = table.col_values(2)

print()
def f(*args,a=1):
    print(args)
    print(a)

f(5,37428,)
a = [4,5,6,7,3,2,6,9,8]

def sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums

print(sort(a))