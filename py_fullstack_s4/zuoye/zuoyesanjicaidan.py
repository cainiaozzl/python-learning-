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

last_layer = [ menu ]

current_layer = menu #当前层

while True:
    for key in current_layer:
        print(key)

    choice = input(">>:").strip()
    if len(choice)==0:continue

    if choice in current_layer: #进入下一层

        last_layers.append(current_layer) #当前层添加到列表
        current_layer = current_layer[choice]
    if choice == "b":
        if last_layers:
            current_layer = last_layers[-1] #取上一层,赋值给current_layer，
            last_layers.pop()
    if choice == "q":
        break


