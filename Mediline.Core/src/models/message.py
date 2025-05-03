from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Text, Column, ForeignKey, Index

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    content = db.Column(Text, nullable=False)
    base_user_id = db.Column(Integer, ForeignKey('base_users.id', ondelete='CASCADE'), nullable=False)

    # Relationships
    base_user = relationship('BaseUser', back_populates='messages')
    appointment_message_assignments = relationship('AppointmentMessageAssignment', back_populates='message')

    # Index for optimization
    __table_args__ = (
        Index('fk_messages_base_users_base_user_id', 'base_user_id'),
    )

    def __repr__(self):
        return f'<Message {self.id} - User {self.base_user_id}>'