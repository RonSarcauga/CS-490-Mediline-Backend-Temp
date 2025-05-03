from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Text, Column
from typing import List

class Medication(db.Model):
    __tablename__ = 'medications'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    medication_name = db.Column(Text, nullable=False)

    # Relationships
    pharmacy_inventory = relationship('PharmacyInventory', back_populates='medication')
    prescribed_medications = relationship('PrescribedMedications', back_populates='medication')

    def __repr__(self):
        return f'<Medication {self.medication_name}>'