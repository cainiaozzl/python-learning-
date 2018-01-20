# count=1
# while True:
#     if count <= 10:
#         input("please input number:")
#         count+=1
#         continue
#     else:
#         break

#使用while循环输入 1 2 3 ... 8 9 10:
count = 0
while True:
    if count < 10:
        count +=1
        print(count)
    else:
        break

#输出 1-100之和：
i = 1
total = 0
while i <101 :
    total = total + i
    i += 1
print(total)

# u = 0
# for i in range(0,100):
#     i += 1
#     u = u + i
# print(u)

#输出 1-100 内的所有奇数:
for i in range(1,100,2):
    print(i)

#输出 1-100 内的所有偶数:
for i in range(2,101,2):
    print(i)


#求1-2+3-4 ... 99的所有数的和:

num = 0

for i in range(100):
    if i % 2 == 0:
        num = num - i
    else:
        num = num + i
print(num)