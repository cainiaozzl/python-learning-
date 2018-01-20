from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,UniqueConstraint,Index,VARCHAR
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine
import pymysql

Base = declarative_base()

def create_db():
    engine = create_engine("mysql+pymysql://root:xpython2017@127.0.0.1:3306/day62?charset=utf8", max_overflow=5)
    Base.metadata.create_all(engine)

def drop_db():
    engine = create_engine("mysql+pymysql://root:xpython2017@127.0.0.1:3306/day62?charset=utf8", max_overflow=5)
    Base.metadata.drop_all(engine)

class UserType(Base):
    __tablename__='usertype'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(VARCHAR(32),nullable=True,index=True)


class User(Base):
    __tablename__='users'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32),nullable=True,default='sf',index=True)
    email = Column(String(16),unique=True)

engine = create_engine("mysql+pymysql://root:xpython2017@127.0.0.1:3306/day62?charset=utf8", max_overflow=5)
Session = sessionmaker(bind=engine)
session = Session()

#类-->表
#对象-->行
#orm add增
# odj1=UserType(title='普通用户')
# session.add(odj1)
#
# objs=[
#     UserType(title='超级用户'),
#     UserType(title='白金用户'),
#     UserType(title='黑金用户'),
# ]
# session.add_all(objs)
#
# session.commit()
# session.close()

###查找：不用commit
#user_typelist=session.query(UserType).all()
#==>select * from usertype
# print(user_typelist)
# print(user_typelist[0])
#user_typelist=session.query(UserType).filter(UserType.id >2)
#==>select * from usertype where id > 2

# for row in user_typelist:
#     print(row.id,row.title)


##删除:
# user_typelist=session.query(UserType).filter(UserType.id >2).delete()
# session.commit()

#--修改--
#修改全部
#session.query(UserType.id,UserType.title).filter(UserType.id>0).update({'title':'黑金'})

#修改特定,字符串类型:
session.query(UserType.id,UserType.title).filter(UserType.id>0).update({UserType.title:UserType.title + "x"},synchronize_session=False)

#修改特定,数字类型
#session.query(UserType.id,UserType.title).filter(UserType.id>0).update({"num":Users.num + 1},synchronize_session="evaluate")

session.commit()