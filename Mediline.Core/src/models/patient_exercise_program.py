from src import db
from sqlalchemy import Integer, Text, DateTime, Enum, Column, text, Boolean

class PatientExerciseProgram(db.Model):
    __tablename__ = 'patient_exercise_programs'
    __table_args__ = {'extend_existing': True}  # Ensures SQLAlchemy recognizes the view

    patient_id = db.Column(Integer)
    program_id = db.Column(Integer, server_default=text("'0'"))
    status = db.Column(Enum('Active', 'Completed'), server_default=text("'Active'"))
    assigned_date = db.Column(DateTime, server_default=text("'CURRENT_TIMESTAMP'"))
    exercise_name = db.Column(Text)
    exercise_type = db.Column(Text)
    reps = db.Column(Text)
    time = db.Column(Text)
    completed = db.Column(Boolean, server_default=text("'0'"))  # Converted TinyInt to Boolean

    def __repr__(self):
        return f'<PatientExerciseProgram {self.program_id} - {self.status}>'