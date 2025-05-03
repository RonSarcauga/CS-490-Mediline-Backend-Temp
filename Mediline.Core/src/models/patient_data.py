from src import db
from sqlalchemy import Integer, Text, DateTime, Date, Column, text

class PatientData(db.Model):
    __tablename__ = 'patient_data'
    __table_args__ = {'extend_existing': True}  # Ensures SQLAlchemy recognizes the view

    user_id = db.Column(Integer, server_default=text("'0'"))
    first_name = db.Column(Text)
    last_name = db.Column(Text)
    sex = db.Column(Text)
    date_of_birth = db.Column(Date)
    email = db.Column(Text)
    phone_number = db.Column(Text)
    city = db.Column(Text)
    state = db.Column(Text)
    postal_code = db.Column(Text)
    role = db.Column(Text)
    create_date = db.Column(DateTime, server_default=text("'CURRENT_TIMESTAMP'"))
    patient_id = db.Column(Integer, server_default=text("'0'"))
    patient_mrn = db.Column(Text)

    def __repr__(self):
        return f'<PatientData {self.patient_id} - {self.first_name} {self.last_name}>'