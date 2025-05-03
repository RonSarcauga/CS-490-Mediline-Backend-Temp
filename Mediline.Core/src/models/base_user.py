from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Text, Date, DateTime, func

class BaseUser(db.Model):
    __tablename__ = 'base_users'  # Matches the MySQL table name

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(Text, nullable=False)
    last_name = db.Column(Text, nullable=False)
    sex = db.Column(Text, nullable=False)
    email = db.Column(Text, nullable=False, unique=True)  # Enforcing unique emails
    phone_number = db.Column(Text, nullable=False, unique=True)
    city = db.Column(Text, nullable=False)
    state = db.Column(Text, nullable=False)
    postal_code = db.Column(Text, nullable=False)
    role = db.Column(Text, nullable=False)
    password = db.Column(Text, nullable=False)
    date_of_birth = db.Column(Date, nullable=False)
    address = db.Column(Text, nullable=False)
    create_date = db.Column(DateTime, default=func.current_timestamp())

    # Relationships
    pharmacists = relationship('Pharmacists', back_populates='base_user')
    discussion_posts = relationship('DiscussionPosts', back_populates='author')
    discussion_profiles = relationship('DiscussionProfiles', back_populates='base_user')
    doctors = relationship('Doctors', back_populates='base_user')
    messages = relationship('Messages', back_populates='base_user')
    patients = relationship('Patients', back_populates='base_user')
    replies = relationship('Replies', back_populates='base_user')

    def __repr__(self):
        return f'<BaseUser {self.first_name} {self.last_name}>'