from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, Date, Text, Numeric, Float, \
    DateTime, REAL, or_, and_, func
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from app import app_config


engine = create_engine(app_config['SQLALCHEMY_URL'], convert_unicode=True, encoding='utf8')

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id'), primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), unique=True, nullable=False)
    name = Column(String(20), unique=False, nullable=False)

    def to_dict(self):  # 將數據轉為字典
        dictionary = self.__dict__
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def __repr__(self):  # 讓print這個物件的時候，看起來好看
        return '<User %r>' % self.username


class UserDetail(Base):
    __tablename__ = 'user_detail'
    id = Column(Integer, Sequence('user_detail_id'), primary_key=True)
    user_id = Column(Integer, unique=True, nullable=False)
    email = Column(String(80), unique=False, nullable=True)


if __name__ == '__main__':
    # Base.metadata.create_all(bind=engine)
    # print('Initialize database.')

    # insert_user = User(username='admin',
    #                 password='admin_password',
    #                 name='admin_name')
    # db_session.add(insert_user)
    # db_session.commit()
    #
    # print(insert_user.id, insert_user.username, insert_user.password, insert_user.name)
    #
    # insert_detail = UserDetail(user_id=insert_user.id,
    #                            email='abcd@efg.com')
    # db_session.add(insert_detail)
    # db_session.commit()

    q = User.query.first()
    print(q)
    print("id: {}, username: {}, password: {}, name: {}".format(q.id, q.username, q.password, q.name))
    print('----------')

    q_all = User.query.all()
    print(q_all)
    for q in q_all:
        print("id: {}, username: {}, password: {}, name: {}".format(q.id, q.username, q.password, q.name))
    print('----------')

    q_filter = User.query.filter(User.id == 2).all()
    print(q_filter)
    print('----------')

    q_order = User.query.order_by(User.id.desc()).all()
    print(q_order)
    print('----------')

    q_join = db_session.query(User, UserDetail).join(UserDetail, UserDetail.user_id == User.id).all()
    print(q_join)
    for user, detail in q_join:
        print(user, detail)
        print("id: {}, username: {}, password: {}, name: {}, email: {}"
              .format(user.id, user.username, user.password, user.name, detail.email))
    print('----------')

    q = User.query.filter(User.id.in_([2, 3])).order_by(User.id.desc()).all()
    print(q)
    print('----------')

    q = User.query.filter(User.id.in_([2, 3])).order_by(User.id.desc())
    print(q)
    print('----------')

