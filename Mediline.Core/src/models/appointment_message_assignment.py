from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, ForeignKey, Index

class AppointmentMessageAssignment(db.Model):
    __tablename__ = 'appointment_message_assignments'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    appointment_id = db.Column(Integer, ForeignKey('appointments.id', ondelete='CASCADE'), nullable=False)
    message_id = db.Column(Integer, ForeignKey('messages.id', ondelete='CASCADE'), nullable=False)

    # Relationships
    appointment = relationship('Appointment', back_populates='appointment_message_assignments')
    message = relationship('Message', back_populates='appointment_message_assignments')

    # Index for optimization
    __table_args__ = (
        Index('fk_appointment_message_assignments_messages', 'message_id'),
    )

    def __repr__(self):
        return f'<AppointmentMessageAssignment {self.id}>'