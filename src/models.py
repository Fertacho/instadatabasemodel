import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import LargeBinary
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    liked_id = Column(Integer, ForeignKey('liked.id'))
    post = relationship(Post)
    comment = relationship(Comment)
    
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    image = Column(LargeBinary, nullable = True)
    content = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    comment_id=Column(Integer, ForeignKey('comment.id'))
    liked = relationship(Liked)

class Comment(Base):
    __tablename__='comment'
    id = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post = relationship(Post)

class Liked(Base):
    __tablename__='liked'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e