
#name = "alex" #加上引号，代表字符
age = 56 #加“”号
user_guess = int( input("input your guess:") ) #默认接受的是字符串,所以前面要加int方法转化成int
print(type(user_guess))
if user_guess > age :
    print("try smaller...")
elif user_guess < age:
    print("try bigger...")
else:

    print("you got it!")
    '''
age = 56 + 5
print(age)
name = "da" + "vid"
print(name)
'''
