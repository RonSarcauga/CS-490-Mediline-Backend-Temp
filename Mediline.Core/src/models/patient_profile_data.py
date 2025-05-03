from src import db
from sqlalchemy import Integer, Text, DateTime, Date, Column, Enum, text

class PatientProfileData(db.Model):
    __tablename__ = 'patient_profile_data'
    __table_args__ = {'extend_existing': True}  # Ensures SQLAlchemy recognizes the view

    user_id = db.Column(Integer, server_default=text("'0'"))
    first_name = db.Column(Text)
    last_name = db.Column(Text)
    date_of_birth = db.Column(Date)
    email = db.Column(Text)
    phone_number = db.Column(Text)
    city = db.Column(Text)
    state = db.Column(Text)
    postal_code = db.Column(Text)
    patient_id = db.Column(Integer, server_default=text("'0'"))
    patient_mrn = db.Column(Text)
    latest_height = db.Column(Text)  # Converted MEDIUMTEXT to Text for compatibility
    latest_weight = db.Column(Text)  # Converted MEDIUMTEXT to Text for compatibility
    prescription_id = db.Column(Integer)
    medication_name = db.Column(Text)
    dosage = db.Column(Text)
    duration = db.Column(Text)
    prescribed_date = db.Column(DateTime)
    status = db.Column(Enum('Prescribed', 'Filled', 'Completed'))

    def __repr__(self):
        return f'<PatientProfileData {self.patient_id} - {self.first_name} {self.last_name}>'