# for i in range(10):
#     if i <= 5:
#         print(i)
#     else:
#         break　#跳出本层循环
#         print("----")


# for i in range(10):
#     if i > 5:
#         print(i)
#     else:
#         continue #跳出本次循环 #这里用ｂｒｅａｋ的话不打印，直接跳出了
#         print("----")

# for i in range(10):
#     print("i",i)
#
#     if i > 5:
#         for j in range(10):
#             if j == 3:
#                 break
#             print("------j",j)

# for i in range(10):
#     print(i)
# else:
#     print("----")
# print("---2")

for i in range(10):
    print(i)
    if i== 5:
        break
else: #当循环正常结束时,走else
    print("done")

print("done2")
