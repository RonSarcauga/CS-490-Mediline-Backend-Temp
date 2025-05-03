from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Text, Date, ForeignKey, Index

class Patient(db.Model):
    __tablename__ = 'patients'  # Matches MySQL table name

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    mrn = db.Column(Text, nullable=False)
    sex = db.Column(Text, nullable=False)
    base_user_id = db.Column(Integer, ForeignKey('base_users.id', ondelete='CASCADE'), nullable=False)
    doctor_id = db.Column(Integer, ForeignKey('doctors.id', ondelete='SET NULL'), nullable=True)
    pharmacy_id = db.Column(Integer, ForeignKey('pharmacies.id', ondelete='SET NULL'), nullable=True)

    # Relationships
    base_user = relationship('BaseUser', back_populates='patients')
    doctor = relationship('Doctor', back_populates='patients_')
    pharmacy = relationship('Pharmacy', back_populates='patients')
    exercise_programs = relationship('ExercisePrograms', back_populates='patient')
    invoices = relationship('Invoices', back_populates='patient')
    prescriptions = relationship('Prescriptions', back_populates='patient')

    # Indexes for optimization
    __table_args__ = (
        Index('fk_patients_base_users', 'base_user_id'),
        Index('fk_patients_doctors', 'doctor_id'),
        Index('fk_patients_pharmacies', 'pharmacy_id'),
    )

    def __repr__(self):
        return f'<Patient MRN: {self.mrn}>'