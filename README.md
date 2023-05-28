DebtsAPI

DebtsAPI is a RESTful API built using Flask, SQLite, and apache2 allowing users to track their debts and manage them.

Features

Allows users to view, add, and modify debts
Calculates interest rate compounding at a rate of 2% per month
Supports user authentication and authorization
Includes unit tests for the API routes and functionality


Project Structure

debts-api/

├── app/

│   ├── __init__.py

│   ├── auth.py

│   ├── models.py

│   ├── routes.py

│   ├── user.py

│   └── utils.py

├── tests/

│   └── test_routes.py

├── config.py

├── requirements.txt

├── .gitignore

├── README.md

└── main.py


app/
The app/ directory contains the core application files:

__init__.py: Initializes the Flask application and sets up any necessary configurations.
auth.py: Provides authentication-related functionality, such as user registration, login, and authorization checks.
models.py: Defines the database models and schema for debts (SQLAlchemy).
routes.py: Contains the API routes/endpoints, where you define the functions handling various HTTP requests and responses.
user.py: Defines the User class for user authentication.
utils.py: Contains utility functions or helper methods used throughout the application.
tests/
The tests/ directory contains unit tests for the API routes and functionality.

config.py
The config.py file holds configuration variables for the application, such as database connection details or secret keys.

requirements.txt
The requirements.txt file lists the required dependencies for the project, including Flask and any other libraries used.

.gitignore
The .gitignore file specifies files and directories that should be ignored by Git when committing and pushing changes.

README.md
The README.md file contains documentation and instructions for setting up and using the DebtsAPI.

main.py
The main.py file acts as the entry point of the application. It initializes the Flask app and runs it using the Flask development server.


Usage

Clone the repository to your local machine.

Make a virtual enviroment for this project.

Install the required dependencies using pip install -r requirements.txt.

Create the database by running python.

Run the application using python main.py.

Use the API endpoints to interact with the DebtsAPI.

API Endpoints


Debt Management

HTTP Method	Endpoint	Description

GET	/api/debts	Retrieves a list of all debts.

GET	/api/debts/{debt_id}	Retrieves a specific debt.

POST	/api/debts	Adds a new debt.

PUT	/api/debts/{debt_id}	Updates an existing debt.

DELETE	/api/debts/{debt_id}	Deletes an existing debt.


User Management

HTTP Method	Endpoint	Description

POST	/api/users	Registers a new user.

POST	/api/login	Logs in an existing user.


License

This project is licensed under the MIT License. See the LICENSE file for details.


