#对象.方法()

a=1
b=a
a=2
print(a)

print(0 and 2)

#转义
s1='Let\'s go'
print(r"\fsdgh1fjdk.")

#查找:[:]
s1 = "hello world"

print(s1[1:4])
print(s1[:])
print(s1[1:])
print(s1[1:-1])
print(s1[-3:-1])

#strip():把字符串开头和结尾的空格以及\n
s=" hello\nworld\n"
s1=" hello\nworld\n".strip()
print(s)
print(s1)

#拼接方法

s="hello" + "world" + "I" + "am" + "python!"

print(s)

print(" ".join(["I","am","world!"]))

#分割方法
s="hello world".split("l")
print(s)

#查找字符
print("hello world".find("l",3))
print("hello world".rfind("l",))

#index
print("hello world".index("o")) #类似find，但有区别

#replace
print("hello world".replace("world","Python"))

#居中显示
print("hello world".center(50,"*"))
print("hello world".ljust(50,"*"))

#字符串的格式化输出

print("hello %s"%"sb")
print("hello %s,%s"%("sb","david"))
print("hello %s,his age is %s"%("sb",35))
print("hello %s,his age is %.4f"%("sb",35))


#"hello world".format()格式化

print("hello {0},his age is {1}".format("alex",34))
print("hello {0},his age is {1}".format(34,"alex"))

print("hello {name},his age is {age}".format(name="david",age=34)) #推荐

print("hello {name},his age is {age}".format_map({"name":"egon","age":1000}))


print("12".isdecimal())
print("12".isdigit())
print("12".isnumeric())

print("一".isdecimal())
print("一".isdigit())
print("一".isnumeric())
print("壹".isnumeric())
print("hello world".capitalize())
print("hello world".title())

print("HELLO world".casefold())
print("HELLO world".lower())

print("HELLO\tworld")
print("HELLO world".expandtabs())

print("HELLO world".rsplit())
print("HELLO\n world\n".split("\n"))
print("HELLO\nworld\n".splitlines())

print("HELLO world".zfill(50))
