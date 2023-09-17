#!/usr/bin/python3
"""
Lists all the State object containing letter a
"""


from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    get_session = session()

    for states in get_session.query(State).order_by(State.id):
        if "a" in states.name:
            print("{}: {}".format(states.id, states.name))

    get_session.close()
