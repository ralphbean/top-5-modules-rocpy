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

    ed_user = create_user()

    print ed_user.id  # None

    print "** Adding user to session."
    session.add(ed_user)

    our_user = session.query(User).filter_by(name='ed').first()
    print "** Are users equal?", ed_user is our_user

    print "** Comitting session."
    session.commit()

    print "** Printing ed_user id:"
    print ed_user.id  # 1

