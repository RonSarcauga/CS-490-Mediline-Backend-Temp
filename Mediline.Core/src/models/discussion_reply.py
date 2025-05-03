from src import db
from sqlalchemy import Integer, Text, DateTime, Column, text

class DiscussionReplies(db.Model):
    __tablename__ = 'discussion_replies'
    __table_args__ = {'extend_existing': True}  # Ensures SQLAlchemy recognizes the view

    reply_id = db.Column(Integer, server_default=text("'0'"))
    post_id = db.Column(Integer)
    base_user_id = db.Column(Integer)
    content = db.Column(Text)
    created_date = db.Column(DateTime)
    time_stamp = db.Column(Text)
    first_name = db.Column(Text)
    last_name = db.Column(Text)

    def __repr__(self):
        return f'<Reply {self.reply_id} - {self.content[:50]}...>'