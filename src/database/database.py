
from sqlalchemy import Column, String, Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
import static

class Database:
    def __init__(self):
        self.engine = create_engine(f"sqlite:///{static.DATABASE_NAME}")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(self.engine)
        self.commit()

    def commit(self):
        self.session.commit()

    def close(self):
        self.engine.dispose()



class Articles(Base):
    __tablename__ = 'articles'

    id = Column(String(30), primary_key=True)
    title = Column(String(100), unique=True)
    link = Column(String(500))

    def __init__(self, id, title, link):
        self.id = id
        self.title = title
        self.link = link



