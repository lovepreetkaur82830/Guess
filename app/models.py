import random
from connect import SessionLocal, Base
from sqlalchemy import Boolean, Integer, Column, ForeignKey, String, Enum

class Word(Base):
    __tablename__ = 'words'

    word = Column(String(5), primary_key=True)
    difficulty = Column(Enum('Easy', 'Medium', 'Difficult'))

    def __repr__(self):
        return f"<Word(word='{self.word}', difficulty='{self.difficulty}')>"

class WordPoolModel:
    def __init__(self):
        pass

    def fetch_word_pool(self):
        session = SessionLocal()
        words = session.query(Word).all()
        session.close()
        return words

    def get_random_word(self):
        word_pool = self.fetch_word_pool()
        random_word = random.choice(word_pool)
        return random_word.word, random_word.difficulty
