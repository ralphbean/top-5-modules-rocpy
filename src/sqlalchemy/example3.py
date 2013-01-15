from example1 import User
from example1 import Base

from example2 import create_model

from sqlalchemy import create_engine

# Creating an instance
def create_user():
    print "Creating user:"
    ed_user = User('ed', 'Ed Jones', 'edspassword')
    print ed_user.name  # 'ed'
    print ed_user.password  # 'edspassword'
    print ed_user.id  # None
    return ed_user

if __name__ == '__main__':
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///:memory:', echo=True)
    create_model(engine)
    ed_user = create_user()
