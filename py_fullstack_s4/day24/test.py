import os
g=os.walk('/tmp/test')

for i in g:
    print(i)
    for j in i[-1]:
        file_path = '%s/%s' %(i[0],j)
        print(file_path)