
def select(data):
    #查询语法一：select name,age from staff_table where age > 22
    #查询语法二：select * from staff_table where dept = IT
    data1 = data.split(" ")
    directory = ["staff_id", "name", "age", "phone", "dept", "enroll-date"]
    if data == ("select name,age from staff_table where age > %s" %(data1[7])):
                with open("xinxi", encoding="utf-8") as f:
                    list = []
                    list1 = []
                    list2 = []
                    for line in f:
                        i = line.strip().split(",")
                        w = i[1]
                        e = i[2]
                        a = [w, e]
                        if e > data1[7]:
                            list2.append(a)
                    for i in list2:
                        print(i)
                    print("查询到 %s 条符合的信息" %len(list2))
    else:
         with open("xinxi", encoding="utf-8") as f:
             list = []
             for line in f:
                 i = line.strip().split(",")
                 q = i[0]
                 w = i[1]
                 e = i[2]
                 r = i[3]
                 t = i[4]
                 y = i[5]
                 if data == ("select * from staff_table where %s = %s" % (data1[5],
                 i[(directory.index(data1[5]))])):
                         list.append(i)
                 else:
                     continue
             for j in list:
                  print('.'.join(j))
             print("查询到 %s 条符合的信息" %len(list))
             return 0

def add():
    pass


def delete():
    pass


def update():
    pass

if __name__ == "__main__":
    msg = """
    1:查询
    2:添加
    3:删除
    4:修改
    5:退出
    """
    msg_dict = {
        "1": select,
        "2": add,
        "3": delete,
        "4": update,
        "5": exit,
    }
    while True:
        print(msg)
        choice = input("输入序号>>:")
        if len(choice) == 0 or choice not in msg_dict: continue
        if choice =='5':break
        data = input("请输入数据>>:").strip()
        msg_dict[choice](data)
