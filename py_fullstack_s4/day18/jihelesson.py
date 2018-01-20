
#集合set 两个功能:1去重　２关系测试

s=set([1,3,"hello"])
s2={1,2,3}

print(s)
print(type(s2))

#去重
l=[1,2,2,34,45]
s="hello"
print(set(l))
print(set(s))

#print({{1,2}:"hello"})
#print({[]:"hello"}) #set是可变数据类型

#s3={1,2,[1,2]} #set 集合内元素一定是不可变数据类型
#print(s3)


#关系测试
s1={"hello",1,2,3}
s2={1,2,("a","b")}

#求并集
s1={"hello",1,2,3}

s2={1,2,("a","b")}

#求并集

print(s1.union(s2))
print(s1|s2)

#求交集
print(s1.intersection(s2))
print(s1&s2)

#求差集
print(s1.difference(s1))
print(s2-s1)

#对称差集

print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))
print(s1^s2)