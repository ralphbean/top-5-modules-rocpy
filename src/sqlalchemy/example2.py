from example1 import User

# Creating an engine
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)


# Creating our tables.
def create_model(engine):
    Base.metadata.create_all(engine)


# Creating an instance
def create_user():
    ed_user = User('ed', 'Ed Jones', 'edspassword')
    ed_user.name
    #'ed'
    ed_user.password
    #'edspassword'
    str(ed_user.id)
    #'None'

# Creating a session
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()


# Using a session
def create_and_add_user():
    ed_user = User('ed', 'Ed Jones', 'edspassword')
    session.add(ed_user)
    our_user = session.query(User).filter_by(name='ed').first()
    print ed_user is our_user  # True!
    print ed_user.id
    session.commit()
    print ed_user.id

# Iterating over queries
# Advanced filtering
# Relationships
from sqlalchemy import ForeignKey
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

# lazy loading
# eager loading

# transactions

# advanced uses
#   introspection       (tw2.jit)
#   reflection          (slurchemy)
#   session extensions  (apply)
