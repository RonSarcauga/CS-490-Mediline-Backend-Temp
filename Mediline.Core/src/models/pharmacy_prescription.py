from src import db
from sqlalchemy import Integer, Text, DateTime, Enum, String, Column, text

class PharmacyPrescriptions(db.Model):
    __tablename__ = 'pharmacy_prescriptions'
    __table_args__ = {'extend_existing': True}  # Ensures SQLAlchemy treats this as a view

    patient_id = db.Column(Integer)
    prescription_id = db.Column(Integer)
    medication_name = db.Column(Text)
    dosage = db.Column(Text)
    duration = db.Column(Text)
    prescribed_date = db.Column(DateTime)
    status = db.Column(Enum('Prescribed', 'Filled', 'Completed'))
    pharmacy_id = db.Column(Integer, server_default=text("'0'"))
    pharmacy_name = db.Column(String(255))

    def __repr__(self):
        return f'<PharmacyPrescription {self.prescription_id} - {self.medication_name}>'