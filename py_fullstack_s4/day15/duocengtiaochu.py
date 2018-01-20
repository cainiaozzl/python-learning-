break_flag = False

for i in range(10):

    print("爷爷层",i)

    for j in range(10):
        print("=爸爸层",j)

        if j == 3:
            break_flag = True
            break

        for k in range(10):
            print("==孙子层",k)
            if k == 2:
                break_flag = True
                break

        if break_flag:
            break
              #exit()
            #flag
    if break_flag: #if break_flag == True:
        print("我儿子死了，我也不活了")
        break
print("keep going....")
