from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Text, DECIMAL, Column
import decimal
from typing import List

class Treatment(db.Model):
    __tablename__ = 'treatments'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    treatment_type = db.Column(Text, nullable=False)
    amount = db.Column(DECIMAL(10, 2), nullable=False)

    # Relationships
    appointments = relationship('Appointment', back_populates='treatment')

    def __repr__(self):
        return f'<Treatment {self.id} - {self.treatment_type}>'