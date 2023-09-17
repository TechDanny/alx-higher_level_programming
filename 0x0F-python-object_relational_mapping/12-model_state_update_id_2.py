#!/usr/bin/python3
"""
Changes the name of object
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

    states = get_session.query(State).filter_by(id=2).first()
    states.name = "New Mexico"
    get_session.commit()

    get_session.close()
