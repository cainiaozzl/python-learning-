
while 1:
    m=input('please input url1:').strip()

    l=[]

    flag=False

    with open("haproxy.conf",encoding="utf8") as f_read:

        for line in f_read:

            if line.strartwith("backend") and m in line:
                flag = True
                continue

            if line.startswith("backend") and flag:
                break

            if flag:

                l.append(line.strip())


        for i in l:
            print(i)




