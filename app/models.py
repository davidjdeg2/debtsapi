from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Debt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    debtor = db.Column(db.String(255), nullable=False)
    amount_owed = db.Column(db.Float, nullable=False)
    interest_rate = db.Column(db.Float, nullable=False, default=0.02)
    date_incurred = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Debt {self.id}>'

    def add_to_debt(self, amount):
        self.amount_owed += amount
        self.date_incurred = datetime.utcnow()

    def subtract_from_debt(self, amount):
        self.amount_owed -= amount
        self.date_incurred = datetime.utcnow()

    def calculate_interest(self, months):
        return self.amount_owed * (1 + self.interest_rate) ** months - self.amount_owed
