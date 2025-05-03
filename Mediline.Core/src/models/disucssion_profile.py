from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Text, Column, ForeignKey, Index

class DiscussionProfile(db.Model):
    __tablename__ = 'discussion_profiles'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    bio = db.Column(Text, nullable=True)
    base_user_id = db.Column(Integer, ForeignKey('base_users.id', ondelete='CASCADE'), nullable=False)

    # Relationships
    base_user = relationship('BaseUser', back_populates='discussion_profiles')

    # Index for optimization
    __table_args__ = (
        Index('fk_discussion_profiles_base_users_base_user_id', 'base_user_id'),
    )

    def __repr__(self):
        return f'<DiscussionProfile {self.id} - {self.base_user_id}>'