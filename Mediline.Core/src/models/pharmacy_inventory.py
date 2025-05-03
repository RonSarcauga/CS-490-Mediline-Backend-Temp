from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, ForeignKey, Index, text

class PharmacyInventory(db.Model):
    __tablename__ = 'pharmacy_inventory'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    pharmacy_id = db.Column(Integer, ForeignKey('pharmacies.id', ondelete='CASCADE'), nullable=False)
    medication_id = db.Column(Integer, ForeignKey('medications.id', ondelete='CASCADE'), nullable=False)
    stock = db.Column(Integer, server_default=text("'100'"), nullable=False)

    # Relationships
    pharmacy = relationship('Pharmacy', foreign_keys=[pharmacy_id], back_populates='pharmacy_inventory')
    medication = relationship('Medication', back_populates='pharmacy_inventory')

    # Indexes for optimization
    __table_args__ = (
        Index('fk_pharmacy_inventory_medications', 'medication_id'),
        Index('fk_pharmacy_inventory_pharmacies', 'pharmacy_id'),
    )

    def __repr__(self):
        return f'<PharmacyInventory {self.id} - Medication {self.medication_id} - Stock {self.stock}>'