from src import db
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, ForeignKey, Index

class Pharmacist(db.Model):
    __tablename__ = 'pharmacists'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    pharmacy_id = db.Column(Integer, ForeignKey('pharmacies.id', ondelete='CASCADE'), nullable=False)
    base_user_id = db.Column(Integer, ForeignKey('base_users.id', ondelete='CASCADE'), nullable=False)

    # Relationships
    base_user = relationship('BaseUser', back_populates='pharmacists')
    pharmacy = relationship('Pharmacy', foreign_keys=[pharmacy_id], back_populates='pharmacists')

    # Indexes for optimization
    __table_args__ = (
        Index('fk_pharmacists_base_users', 'base_user_id'),
        Index('fk_pharmacists_pharmacies', 'pharmacy_id'),
    )

    def __repr__(self):
        return f'<Pharmacist {self.id} - BaseUser {self.base_user_id}>'