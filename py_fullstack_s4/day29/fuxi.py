class People:
    def __init__(self,name,sex,age):
        self.name=name
        self.age=age
        self.sex=sex

    def walk(self):
        print('%s is walking' %self.name)

class Chinese(People):
    country='China'
    def __init__(self,name,sex,age,language='Chinese'):
        # self.name=name
        # self.sex=sex
        # self.age=age
        People.__init__(self,name,sex,age)
        self.language=language

    def walk(self):
        People.walk(self)
        print('================')


class North_korean(People):
    country='Korean'



c=Chinese('egon','male',22)

print(c.name,c.age,c.sex)

c.walk()

#组合
class Teacher:
    def __init__(self,name,sex,course):
        self.name=name
        self.sex=sex
        self.course=course
class Student:
    def __init__(self,name,sex,course):
        self.name=name
        self.sex=sex
        self.course=course
class Course:
    def __init__(self,name,price,peroid):
        self.name=name
        self.price=price
        self.period=peroid
python_obj=Course('python',15800,'7m')
t1=Teacher('egon','male',python_obj)
s1=Student('cobila','male',python_obj)

print(s1.course.name)
print(t1.course.name)
