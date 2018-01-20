name = "中国"
print(name)
print (type(name))

f = open("test.txt",encoding="utf-8") #默认以utf-8解析
print(name.encode("gbk")) #编码。会把unicode转成相应的编码的同时,同事转为ｂｙｔｅ

print(f.read())