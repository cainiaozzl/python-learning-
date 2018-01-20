break_flag = False

count = 0
while break_flag == False :
    print("爷爷层...")

    while break_flag == False :
        print("爸爸层...")

        while break_flag == False :
            count +=1
            if count >10 :
                break_flag = True

            print("炎龙层...")

print("keep going...")