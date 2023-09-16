#!/usr/bin/python3
"""Print the State object with the given name from the database"""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("""mysql+mysqldb://{}:{}@localhost/{}"""
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        state = session.query(State)
        state = state.filter_by(name=argv[4]).first()
        print("{}".format(state.id))
    except Exception:
        print("Not found")
    session.close()
