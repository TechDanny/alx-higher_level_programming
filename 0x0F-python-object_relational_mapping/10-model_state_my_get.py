#!/usr/bin/python3
"""
prints the ste object with the name
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

    for states in get_session.query(State):
        if argv[4] == states.name:
            print("{}".format(states.id))
            break
    else:
            print("Not found")

    get_session.close()
