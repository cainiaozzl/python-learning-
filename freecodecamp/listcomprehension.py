cubes_by_four = [x ** 3 for x in range(1,11) if ((x**3)%4) == 0]
print(cubes_by_four)

l = [i**2 for i in range(1,11)]
print(l[2:9:2])

my_list = range(1, 11)

# Add your code below!
to_21 = range(1, 22)

odds = to_21[::2]

middle_third = to_21[7:14]

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print filter(lambda x: x == "Python", languages)

squares = [x ** 2 for x in range(1, 11)]

print filter(lambda x: x >= 30 and x <= 70, squares)

threes_and_fives = [x for x in range(1,16) if x%3==0 or x%5==0]
print threes_and_fives


#===========================
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]

message = filter(lambda x: x != "X", garbled)
print message
