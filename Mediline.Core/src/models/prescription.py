from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, DateTime, Enum, Column, ForeignKey, Index, text
import datetime
from typing import List

class Prescription(db.Model):
    __tablename__ = 'prescriptions'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    doctor_id = db.Column(Integer, ForeignKey('doctors.id', ondelete='CASCADE'), nullable=False)
    patient_id = db.Column(Integer, ForeignKey('patients.id', ondelete='CASCADE'), nullable=False)
    prescribed_date = db.Column(DateTime, nullable=False)
    status = db.Column(Enum('Prescribed', 'Filled', 'Completed'), nullable=False)

    # Relationships
    doctor = relationship('Doctor', back_populates='prescriptions')
    patient = relationship('Patient', back_populates='prescriptions')
    prescribed_medications = relationship('PrescribedMedication', back_populates='prescription')

    # Indexes for optimization
    __table_args__ = (
        Index('fk_prescriptions_doctors', 'doctor_id'),
        Index('fk_prescriptions_patients', 'patient_id'),
    )

    def __repr__(self):
        return f'<Prescription {self.id} - Status: {self.status}>'