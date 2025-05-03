from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Text, Column, ForeignKey, Index

class PrescribedMedication(db.Model):
    __tablename__ = 'prescribed_medications'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    prescription_id = db.Column(Integer, ForeignKey('prescriptions.id', ondelete='CASCADE'), nullable=False)
    medication_id = db.Column(Integer, ForeignKey('medications.id', ondelete='CASCADE'), nullable=False)
    dosage = db.Column(Text, nullable=False)
    duration = db.Column(Text, nullable=False)

    # Relationships
    medication = relationship('Medication', back_populates='prescribed_medications')
    prescription = relationship('Prescription', back_populates='prescribed_medications')

    # Indexes for optimization
    __table_args__ = (
        Index('fk_prescribed_medications_medications', 'medication_id'),
        Index('fk_prescribed_medications_prescriptions', 'prescription_id'),
    )

    def __repr__(self):
        return f'<PrescribedMedication {self.id} - Prescription {self.prescription_id}>'