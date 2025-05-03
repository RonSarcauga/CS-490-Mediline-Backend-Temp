from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, DateTime, DECIMAL, Enum, Column, ForeignKey, Index, text
import datetime
import decimal
from typing import Optional

class Invoice(db.Model):
    __tablename__ = 'invoices'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(Integer, ForeignKey('patients.id', ondelete='CASCADE'), nullable=False)
    appointment_id = db.Column(Integer, ForeignKey('appointments.id', ondelete='CASCADE'), nullable=False)
    amount = db.Column(DECIMAL(10, 2), nullable=False)
    issued_date = db.Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), nullable=True)
    status = db.Column(Enum('Pending', 'Paid'), server_default=text("'Pending'"), nullable=True)

    # Relationships
    appointment = relationship('Appointment', back_populates='invoices')
    patient = relationship('Patient', back_populates='invoices')

    # Indexes for optimization
    __table_args__ = (
        Index('fk_invoices_appointments', 'appointment_id'),
        Index('fk_invoices_patients', 'patient_id'),
    )

    def __repr__(self):
        return f'<Invoice {self.id} - Amount: {self.amount} - Status: {self.status}>'