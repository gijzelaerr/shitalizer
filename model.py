
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql://gijs@/gijs', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class Post(Base):
    """
    A shit-list post.
    """
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    message_id = Column(String)
    date = Column(DateTime)
    from_ = Column(String)
    in_reply_to = Column(String)
    subject = Column(String)
    body = Column(String)

    def __init__(self, message_id, date, from_, subject, body, in_reply_to=None):
        self.message_id = message_id
        self.date = date
        self.from_ = from_
        self.subject = subject
        self.body = body
        self.in_reply_to = in_reply_to
