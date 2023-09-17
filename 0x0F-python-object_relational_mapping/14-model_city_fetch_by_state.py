#!/usr/bin/python3
"""
prints all city objects from database
"""


from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_city import City
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    get_session = session()

    for states, cities in get_session.query(State, City).filter(
                          State.id == City.states_unique).all():
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))

    get_session.close()
