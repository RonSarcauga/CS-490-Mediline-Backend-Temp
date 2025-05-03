from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Text, ForeignKey, Index, Boolean

class Doctor(db.Model):
    __tablename__ = 'doctors'  # Matches MySQL table name

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    license_number = db.Column(Text, nullable=False)
    specialty = db.Column(Text, nullable=False)
    patients = db.Column(Text, nullable=False)  # Consider normalizing this into a separate table
    accepting_new_patients = db.Column(Boolean, nullable=False)  # Changed to Boolean for clarity
    base_user_id = db.Column(Integer, ForeignKey('base_users.id', ondelete='CASCADE'), nullable=False)

    # Relationships
    base_user = relationship('BaseUser', back_populates='doctors')
    patients_ = relationship('Patient', back_populates='doctor')
    prescriptions = relationship('Prescription', back_populates='doctor')

    # Indexes for optimization
    __table_args__ = (
        Index('fk_doctors_base_users_base_user_id', 'base_user_id'),
    )

    def __repr__(self):
        return f'<Doctor {self.license_number} - {self.specialty}>'