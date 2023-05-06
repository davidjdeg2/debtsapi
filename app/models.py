from flask import jsonify, request
from .models import Debt, db

@app.route('/debts', methods=['GET'])
def get_debts():
    debts = Debt.query.all()
    return jsonify([debt.__dict__ for debt in debts])

@app.route('/debts/<int:debt_id>/add', methods=['PUT'])
def add_to_debt(debt_id):
    debt = Debt.query.get_or_404(debt_id)
    data = request.get_json()
    amount = data['amount']
    debt.add_to_debt(amount)
    db.session.commit()
    return jsonify(debt.__dict__)

@app.route('/debts/<int:debt_id>/subtract', methods=['PUT'])
def subtract_from_debt(debt_id):
    debt = Debt.query.get_or_404(debt_id)
    data = request.get_json()
    amount = data['amount']
    debt.subtract_from_debt(amount)
    db.session.commit()
    return jsonify(debt.__dict__)

@app.route('/debts/<int:debt_id>/interest', methods=['GET'])
def calculate_interest(debt_id):
    debt = Debt.query.get_or_404(debt_id)
    data = request.args
    months = int(data.get('months', 1))
    interest = debt.calculate_interest(months)
    return jsonify
