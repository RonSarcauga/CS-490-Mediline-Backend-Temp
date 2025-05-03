from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Text, DateTime, Column, ForeignKey, Index
import datetime
from typing import Optional

class Reply(db.Model):
    __tablename__ = 'replies'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(Integer, nullable=False)
    content = db.Column(Text, nullable=False)
    created_date = db.Column(DateTime, nullable=False)
    time_stamp = db.Column(Text, nullable=False)
    base_user_id = db.Column(Integer, ForeignKey('base_users.id', ondelete='CASCADE'), nullable=False)
    discussion_post_id = db.Column(Integer, ForeignKey('discussion_posts.id', ondelete='CASCADE'), nullable=False)
    parent_reply_id = db.Column(Integer, nullable=True)

    # Relationships
    base_user = relationship('BaseUser', back_populates='replies')
    discussion_post = relationship('DiscussionPost', back_populates='replies')

    # Indexes for optimization
    __table_args__ = (
        Index('fk_replies_base_users_base_user_id', 'base_user_id'),
        Index('fk_replies_discussion_posts_discussion_post_id', 'discussion_post_id'),
    )

    def __repr__(self):
        return f'<Reply {self.id} - Post {self.post_id}>'