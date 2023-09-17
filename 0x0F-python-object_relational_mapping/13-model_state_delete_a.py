#!/usr/bin/python3
"""
Deletes all state objects with name 'a'
"""


from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True
                           )

    session = sessionmaker(bind=engine)
    get_session = session()

    all_states = get_session.query(State).filter(State.name.like('%a%')).all()
    for states in all_states:
        get_session.delete(states)
    get_session.commit()

    get_session.close()
