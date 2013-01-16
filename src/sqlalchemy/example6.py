from example1 import User
from example1 import Base
from example2 import create_model
from example3 import create_user
from example4 import create_session

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", backref=backref('addresses', order_by=id))

    def __init__(self, email_address):
        self.email_address = email_address

    def __repr__(self):
        return "<Address('%s')>" % self.email_address


def create_fake_data(session):
    user = User('Bobby B', 'some_password', None)
    session.add(user)
    address = Address('bobby@b.com')
    session.add(address)
    #user.addresses.append(address)
    address.user = user
    session.commit()

if __name__ == '__main__':
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///:memory:', echo=True)
    create_model(engine)
    session = create_session(engine)

    create_fake_data(session)

    some_user = session.query(User).first()
    print "** Got this user:", some_user
    print "**   with addresses:",
    for address in some_user.addresses:
        print "**    ", address

    print address.user
