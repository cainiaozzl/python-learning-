menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{},
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{ },
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{},

            },
        },
        '闸北':{
            '火车站':{
                '携程':{},
            },
        },
        '浦东':{},
    },
    '山东':{...},
}

exit_flag = False
while not exit_flag:
    for key in menu:
        print(key)

    choice = input(">:").strip()
    if len(choice) == 0 : continue
    if choice == 'q':
        exit_flag = True
        continue
    if choice in menu: #省存在，进入此省下一级
        while not exit_flag:
            next_layer = menu[choice]
            for key2 in next_layer:
                print(key2)
            choice2 = input(">>:").strip()
            if len(choice2) == 0:continue
            if choice2 == 'b': break
            if choice2 == 'q':
                exit_flag = True
                continue
            if choice2 in next_layer: #再进入下一层
                while not exit_flag:
                    next_layer2 = next_layer[choice2]
                    for key3 in next_layer2:
                        print(key3)
                    choice3 = input(">>>:").strip()
                    if len(choice3) == 0: continue
                    if choice3 == 'b':break
                    if choice3 == 'q':
                        exit_flag = True
                        continue

                    if choice3 in next_layer2:
                        while not exit_flag:
                            next_layer3 = next_layer2[choice3]
                            for key4 in next_layer3:
                                print(key4)

                            choice4 = input(">>>>:").strip()
                            if choice4 == 'b':break
                            if choice4 == 'q':
                                exit_flag = True
                                continue


