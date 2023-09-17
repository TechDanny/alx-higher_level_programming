#!/usr/bin/python3
"""
adds object to data base
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

    Base.metadata.create_all(engine)

    newObject = State(name="Louisiana")
    get_session.add(newObject)
    get_session.commit()
    print(newObject.id)

    get_session.close()
