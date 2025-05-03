from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Text, DateTime, Column, ForeignKey, Index, text
import datetime
from typing import List

class DiscussionPost(db.Model):
    __tablename__ = 'discussion_posts'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(Integer, ForeignKey('base_users.id'), nullable=False)
    title = db.Column(Text, nullable=False)
    content = db.Column(Text, nullable=False)
    created_date = db.Column(DateTime, nullable=False)
    time_stamp = db.Column(Text, nullable=False)

    # Relationships
    author = relationship('BaseUser', back_populates='discussion_posts')
    replies = relationship('Reply', back_populates='discussion_post')

    # Indexes for optimization
    __table_args__ = (
        Index('fk_discussion_posts_base_users_author_id', 'author_id'),
    )

    def __repr__(self):
        return f'<DiscussionPost {self.id} - {self.title}>'