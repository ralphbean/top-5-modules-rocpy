from example1 import Base

# Creating our tables.
def create_model(engine):
    print "** Creating all tables"
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    # Creating an engine
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///:memory:', echo=True)
    create_model(engine)
