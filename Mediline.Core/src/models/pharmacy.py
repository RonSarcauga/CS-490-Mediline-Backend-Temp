from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Text, String, Column, ForeignKey, Index

class Pharmacy(db.Model):
    __tablename__ = 'pharmacies'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    inventory_id = db.Column(Integer, ForeignKey('pharmacy_inventory.id', ondelete='CASCADE'), nullable=False)
    pharmacist_id = db.Column(Integer, ForeignKey('pharmacists.id', ondelete='CASCADE'), nullable=False)
    address = db.Column(Text, nullable=False)
    city = db.Column(Text, nullable=False)
    zip_code = db.Column(String(10), nullable=False)
    state = db.Column(Text, nullable=False)
    pharmacy_name = db.Column(String(255), nullable=False)

    # Relationships
    inventory = relationship('PharmacyInventory', foreign_keys=[inventory_id], back_populates='pharmacies')
    pharmacist = relationship('Pharmacist', foreign_keys=[pharmacist_id], back_populates='pharmacies')
    pharmacists = relationship('Pharmacist', foreign_keys='[Pharmacist.pharmacy_id]', back_populates='pharmacy')
    pharmacy_inventory = relationship('PharmacyInventory', foreign_keys='[PharmacyInventory.pharmacy_id]', back_populates='pharmacy')
    patients = relationship('Patient', back_populates='pharmacy')

    # Indexes for optimization
    __table_args__ = (
        Index('fk_pharmacies_inventory', 'inventory_id'),
        Index('fk_pharmacies_pharmacists', 'pharmacist_id'),
    )

    def __repr__(self):
        return f'<Pharmacy {self.pharmacy_name} - {self.city}, {self.state}>'