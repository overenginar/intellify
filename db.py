from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Dictionary(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    word = Column(String)
    meaning = Column(String)
    

class DictionaryDb():

    def __init__(self, refresh_db=False) -> None:
        self.refresh_db = refresh_db

    def create_db(self):
        engine = create_engine('sqlite:///dictionary.db')
        Session = sessionmaker(bind=engine)
        session = Session()

        if self.refresh_db:
            Base.metadata.drop_all(engine)
            Base.metadata.create_all(engine)
        return session

    def insert_word(self, session, word, meaning):
        new_word = Dictionary(word=word, meaning=meaning)
        session.add(new_word)
        session.commit()
    
    def get_words(self, session):
        words = session.query(Dictionary).all()
        return words
