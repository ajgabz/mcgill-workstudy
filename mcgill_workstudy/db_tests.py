from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://aarongaba:@localhost/aarongaba')
Base = declarative_base(engine)

class Student(Base):
    student


