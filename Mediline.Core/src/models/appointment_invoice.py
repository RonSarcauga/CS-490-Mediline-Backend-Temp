from src import db
from sqlalchemy import Integer, Text, DateTime, DECIMAL, Enum, Column, text

class AppointmentInvoice(db.Model):
    __tablename__ = 'appointment_invoices'
    __table_args__ = {'extend_existing': True}  # Ensures SQLAlchemy treats this as a view

    appointment_id = db.Column(Integer, server_default=text("'0'"))
    patient_id = db.Column(Text)
    doctor_id = db.Column(Text)
    appoint_start_date = db.Column(DateTime)
    treatment_id = db.Column(Integer)
    treatment_cost = db.Column(DECIMAL(10, 2))
    invoice_id = db.Column(Integer, server_default=text("'0'"))
    invoice_amount = db.Column(DECIMAL(10, 2))
    status = db.Column(Enum('Pending', 'Paid'), server_default=text("'Pending'"))
    issued_date = db.Column(DateTime, server_default=text("'CURRENT_TIMESTAMP'"))

    def __repr__(self):
        return f'<AppointmentInvoice {self.invoice_id} - Status: {self.status}>'