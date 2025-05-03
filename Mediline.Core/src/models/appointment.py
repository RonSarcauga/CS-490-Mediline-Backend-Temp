from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Text, DateTime, Enum, Column, ForeignKey, Index, text
import datetime
from typing import List

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    appointment_type = db.Column(Text, nullable=False)
    doctor_id = db.Column(Text, nullable=False)
    patient_id = db.Column(Text, nullable=False)
    appoint_start_date = db.Column(DateTime, nullable=False)
    appoint_end_date = db.Column(DateTime, nullable=False)
    notes = db.Column(Text, nullable=True)
    pharmacy_notes = db.Column(Text, nullable=True)
    treatment_id = db.Column(Integer, ForeignKey('treatments.id'), nullable=False)
    status_label = db.Column(Enum('Scheduled', 'Canceled', 'Completed'), server_default=text("'Scheduled'"))

    # Relationships
    treatment = relationship('Treatment', back_populates='appointments')
    appointment_message_assignments = relationship('AppointmentMessageAssignment', back_populates='appointment')
    invoices = relationship('Invoice', back_populates='appointment')

    # Indexes for optimization
    __table_args__ = (
        Index('fk_appointments_treatments', 'treatment_id'),
    )

    def __repr__(self):
        return f'<Appointment {self.id} - Status: {self.status_label}>'