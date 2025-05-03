from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Text, DateTime, Enum, Column, ForeignKey, Index, text
import datetime
from typing import List, Optional

class ExerciseProgram(db.Model):
    __tablename__ = 'exercise_programs'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(Integer, ForeignKey('patients.id', ondelete='CASCADE'), nullable=False)
    status = db.Column(Enum('Active', 'Completed'), server_default=text("'Active'"))
    assigned_date = db.Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), nullable=True)

    # Relationships
    patient = relationship('Patient', back_populates='exercise_programs')
    exercise_program_details = relationship('ExerciseProgramDetails', back_populates='exercise_program')

    # Index for optimization
    __table_args__ = (
        Index('fk_exercise_programs_patients', 'patient_id'),
    )

    def __repr__(self):
        return f'<ExerciseProgram {self.id} - Status: {self.status}>'