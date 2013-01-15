from example1 import User
from example2 import create_model
from example3 import create_user
from example4 import create_session


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
