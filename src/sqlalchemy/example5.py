from example1 import User
from example1 import Base

from example2 import create_model

from example3 import create_user


def create_session(engine):
    # Creating a session
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

if __name__ == '__main__':
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///:memory:', echo=True)
    create_model(engine)

    session = create_session(engine)
    one_user = create_user()
    session.add(one_user)
    another_user = create_user()
    session.add(another_user)
    session.commit()

    for some_user in session.query(User):
        print "** Iterating over users"
        print some_user


    print "** Counting all users"
    print session.query(User).count()

    print "** Counting all users another way"
    print len(session.query(User).all())
