from src import db
from sqlalchemy import Integer, Text, DateTime, Column
import datetime

class VitalHistory(db.Model):
    __tablename__ = 'vital_histories'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    patient_mrn = db.Column(Text, nullable=False)
    doctor_license_number = db.Column(Text, nullable=False)
    date = db.Column(DateTime, nullable=False)
    height = db.Column(Text, nullable=False)
    weight = db.Column(Text, nullable=False)
    calories_burned = db.Column(Text, nullable=False)
    water_intake = db.Column(Text, nullable=False)
    blood_pressure = db.Column(Text, nullable=False)
    heart_rate = db.Column(Text, nullable=False)

    def __repr__(self):
        return f'<VitalHistory {self.id} - MRN {self.patient_mrn}>'