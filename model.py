
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, ForeignKey, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()


mail_references = Table('mail_references', Base.metadata,
                        Column('referred_id', Integer, ForeignKey('post.id')),
                        Column('referring_id', Integer, ForeignKey('post.id'))
                        )


class Post(Base):
    """
    A shit-list post.
    """
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    message_id = Column(String, unique=True)
    date = Column(DateTime)
    from_ = Column(String)
    references = relationship('Post', secondary=mail_references,
                              backref='referring')
    in_reply_to = Column(String)
    subject = Column(String)
    body = Column(String)


