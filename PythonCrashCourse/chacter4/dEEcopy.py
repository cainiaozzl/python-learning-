import copy
spam = [['A','B'],'C','D',[1,2,3]]
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(spam)
print('================================spam below')
print(cheese)
