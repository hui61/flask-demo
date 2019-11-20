from db import db


# 用户信息
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)  # id primary key
    name = db.Column(db.String(20), nullable=False)  # user name
    password = db.Column(db.String(42), nullable=False)  # user password

    def __repr__(self):
        return 'User[id=' + str(self.id) + ',name=' + self.name + ',password=' + self.password + ']'
