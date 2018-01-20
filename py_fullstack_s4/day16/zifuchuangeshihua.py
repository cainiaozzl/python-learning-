name = input("name:")
age = input("age:")
job = input("job:")
salary = input("salary:")

info = '''

-----info of %s-----
NAME: %s
AGE: %d
JOB: %s
SALARY:%fRMB
---------end--------
'''% (name,name,int(age),job,int(salary))

print(info)

#%f:float
#%d:digit
#%s:string

