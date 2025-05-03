from src import db
from sqlalchemy import Integer, Text, DateTime, Enum, Column

class PatientPrescriptions(db.Model):
    __tablename__ = 'patient_prescriptions'
    __table_args__ = {'extend_existing': True}  # Ensures SQLAlchemy recognizes the view

    patient_id = db.Column(Integer)
    doctor_id = db.Column(Integer)
    prescription_id = db.Column(Integer)
    medication_name = db.Column(Text)
    dosage = db.Column(Text)
    duration = db.Column(Text)
    prescribed_date = db.Column(DateTime)
    status = db.Column(Enum('Prescribed', 'Filled', 'Completed'))

    def __repr__(self):
        return f'<Prescription {self.prescription_id} - {self.status}>'