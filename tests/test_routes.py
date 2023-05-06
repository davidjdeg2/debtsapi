import json
from .models import db, Debt
from .main import app

def test_get_debt():
    with app.test_client() as client:
        # Create a new debt
        debt = Debt(debtor='Knox Seabolt', amount_owed=.40, interest_rate=4)
        db.session.add(debt)
        db.session.commit()

        # Send a GET request to /debt/1
        response = client.get('/debt/1')
        print(response)

        # Check that the response is successful and has the expected data
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['debtor'] == 'Knox Seabolt'
        assert data['amount_owed'] == .40
        assert data['interest_rate'] == 4
