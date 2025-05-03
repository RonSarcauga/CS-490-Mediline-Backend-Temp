from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Text, Column, ForeignKey, Index, Boolean, text
from typing import Optional

class ExerciseProgramDetail(db.Model):
    __tablename__ = 'exercise_program_details'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    exercise_program_id = db.Column(Integer, ForeignKey('exercise_programs.id', ondelete='CASCADE'), nullable=False)
    exercise_id = db.Column(Integer, ForeignKey('exercises.id', ondelete='CASCADE'), nullable=False)
    reps = db.Column(Text, nullable=True)
    time = db.Column(Text, nullable=True)
    completed = db.Column(Boolean, server_default=text("'0'"), nullable=True)  # Converted TINYINT(1) to Boolean

    # Relationships
    exercise = relationship('Exercise', back_populates='exercise_program_details')
    exercise_program = relationship('ExerciseProgram', back_populates='exercise_program_details')

    # Indexes for optimization
    __table_args__ = (
        Index('fk_exercise_program_details_exercises', 'exercise_id'),
        Index('fk_exercise_program_details_programs', 'exercise_program_id'),
    )

    def __repr__(self):
        return f'<ExerciseProgramDetail {self.id} - Program {self.exercise_program_id}>'