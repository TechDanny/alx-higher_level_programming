#!/usr/bin/python3
"""
Prints the first State of object
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

    states = get_session.query(State).order_by(State.id).first()

    if states is None:
        print("Nothing")
    print("{}: {}".format(states.id, states.name))

    get_session.close()
