#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""

from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("""mysql+mysqldb://{}:{}@localhost/{}"""
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State, City).filter(City.state_id == State.id)
    result = result.order_by(City.id).all()
    for states, city in result:
        print("{}: ({}) {}".format(states.name, city.id, city.name))
    session.close()
