from flask import jsonify, request
from .models import Debt, db

@app.route('/debt/<int:id>', methods=['GET'])
def get_debt(id):
    debt = Debt.query.get(id)
    if not debt:
        return jsonify({'error': 'Debt not found'}), 404
    total_owed = calculate_interest(debt.amount_owed, debt.interest_rate)
    return jsonify({
        'id': debt.id,
        'debtor': debt.debtor,
        'amount_owed': debt.amount_owed,
        'interest_rate': debt.interest_rate,
        'total_owed': total_owed
    }), 200

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
    return jsonify({'interest': interest})
