from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Text, Column
from typing import List, Optional

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    exercise_name = db.Column(Text, nullable=False)
    exercise_type = db.Column(Text, nullable=False)
    description = db.Column(Text, nullable=True)

    # Relationships
    exercise_program_details = relationship('ExerciseProgramDetails', back_populates='exercise')

    def __repr__(self):
        return f'<Exercise {self.exercise_name} - {self.exercise_type}>'