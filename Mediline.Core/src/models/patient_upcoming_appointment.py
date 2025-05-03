from src import db
from sqlalchemy import Integer, Text, DateTime, Enum, Column, text

class PatientUpcomingAppointments(db.Model):
    __tablename__ = 'patient_upcoming_appointments'
    __table_args__ = {'extend_existing': True}  # Ensures SQLAlchemy recognizes the view

    appointment_id = db.Column(Integer, server_default=text("'0'"))
    patient_id = db.Column(Text)
    doctor_id = db.Column(Text)
    appoint_start_date = db.Column(DateTime)
    status_label = db.Column(Enum('Scheduled', 'Canceled', 'Completed'), server_default=text("'Scheduled'"))

    def __repr__(self):
        return f'<UpcomingAppointment {self.appointment_id} - {self.status_label}>'