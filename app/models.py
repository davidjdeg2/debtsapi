from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import warnings

db = SQLAlchemy()

#anti-crust function
def number_verifier(amount):
    if isinstance(amount, (int, float)):
        return return "{:.2f}".format(amount)
    else
        warnings.warn("expected input is a number", RuntimeWarning)

class Debt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    debtor = db.Column(db.String(255), nullable=False)
    amount_owed = db.Column(db.Float, nullable=False)
    interest_rate = db.Column(db.Float, nullable=False, default=0.02)
    date_incurred = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Debt {self.id}>'

    def update_debt(self, amount):
        self.amount_owed += number_verifier(amount)
        self.date_incurred = datetime.utcnow()
        
    def set_debt(self, amount):
        self.amount_owed = number_verifier(amount)
        self.date_incurred = datetime.utcnow()

    def calculate_interest(self, months):
        #string format to round the number to the nearest 2nd decimal place then add a cent to round up
        return "{:.2f}".format(self.amount_owed * (1 + self.interest_rate) ** months - self.amount_owed) + 0.01
