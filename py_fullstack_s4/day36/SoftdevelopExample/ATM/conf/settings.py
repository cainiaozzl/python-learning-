import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_path ='%s /db' %BASE_DIR
print(db_path)