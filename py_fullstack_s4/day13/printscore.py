score = int(input("Input your score:"))
#同一级代码缩进必须一致
#官方建议岁
if score >= 90 and score <= 100:
    print("A")
    choice = input("任何奖励:")
    if choice == "大保健":
        print("秦镇专属...")

elif score >=80:
    print("B")

elif score >=70:
    print("B-")

elif score >= 60:
    print("C+")

elif score >= 50:
    print("C")
