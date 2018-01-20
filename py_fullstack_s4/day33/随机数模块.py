import random


#print(random.random())

#print(random.randint(1,4))  #[1,4]
#print(random.randrange(1,3))  #[1,3)

# print(random.choice([11,26,3,4]))
# print(random.sample([11,26,3,4],2))

#print(random.uniform(1,3))

# item=[1,23,33]
#
# random.shuffle(item)
# print(item)

# a-z  A-Z


def validate():

    s=""
    for i in range(5):
         rNum=random.randint(0,9)
         r_alph=chr(random.randint(65,90))

         ret=random.choice([str(rNum),r_alph])
         s+=ret

    return s

print(validate())

