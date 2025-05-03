from src import db
from sqlalchemy import Integer, Text, DateTime, BigInteger, Column, text

class DiscussionPostData(db.Model):
    __tablename__ = 'discussion_post_data'
    __table_args__ = {'extend_existing': True}  # Prevents SQLAlchemy from modifying the view

    user_id = db.Column(Integer, server_default=text("'0'"))
    first_name = db.Column(Text)
    last_name = db.Column(Text)
    bio = db.Column(Text)
    post_id = db.Column(Integer, server_default=text("'0'"))
    title = db.Column(Text)
    content = db.Column(Text)
    created_date = db.Column(DateTime)
    time_stamp = db.Column(Text)
    reply_count = db.Column(BigInteger)

    def __repr__(self):
        return f'<DiscussionPost {self.post_id} - {self.title}>'