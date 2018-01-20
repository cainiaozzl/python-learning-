product_list = [["Iphone",5800],
               ["coffee",30],
               ['noodle',10],
               ['Python Book',99],
               ['Bike',199],
               ['ViVo X9',2499]
                ]


shopping_cart = {}
salary = int(input("input your salary:"))
while True:
    index = 0
    for product in product_list:
        print(index,product)
        index +=1
    choice = input(">>:").strip()
    if choice.isdigit(): #判断是否为数字
        choice = int(choice)
        if choice >= 0 and choice < len(product_list):
            product = product_list[choice] #取得商品
            if product[1] <= salary:
                #买得起
                if product[0] in shopping_cart: #判断是否买过
                    shopping_cart[product[0]][1] += 1 #[price,数量]加入购物车
                else:
                    shopping_cart[product[0]] = [product[1],1] #创建一条购买记录
                salary -= product[1] #扣钱
                print("Added product" + product[0] + "into shopping cart,\033[31myour current balance is\033[0m:" + str(salary))
                #\033[42;1myour current balance is\033[0m 给字符串设置背景色
            else:
                print("Excuse me,it is " + str(product[1]) + "RMB,you are " + str(product[1]-salary) + "RMB short.")

        else:
            print("This commodity not exist!")

    elif choice == "q":
        print("---Shopping List---")

        id_counter = 1
        total_cost = 0
        print("id  commodity　amount　unit-price　total-price")
        for key in shopping_cart:
            print("%10s%10s%10s%10s%10s" %(id_counter,
                  key,
                  shopping_cart[key][1],
                  shopping_cart[key][0],
                  shopping_cart[key][1]*shopping_cart[key][0]))

            id_counter +=1
            total_cost += shopping_cart[key][1]*shopping_cart[key][0] #单个商品总价

        print("Your total expenditure:",total_cost)
        print("Your balance：",salary)

        print("---end---")
        break
    else:
        print("option not exist")