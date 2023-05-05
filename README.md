# debtsapi
I am very kind to my debtees.

This API implementation on an Ubuntu Server running will return the current amount of debt owed to Knox Seabolt, and for an authenticated user, they can add or modify the array. It utilizes Flask, a python micro web framework.

debt-api/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── auth.py
│   └── utils.py
├── tests/
│   └── test_routes.py
├── config.py
├── requirements.txt
├── .gitignore
├── README.md
└── run.py

app/ directory:

__init__.py: Initializes the Flask application and sets up any necessary configurations.
models.py: Defines the database models and schema for debt and user entities using a library like SQLAlchemy.
routes.py: Contains the API routes/endpoints, where you define the functions handling various HTTP requests and responses.
auth.py: Provides authentication-related functionality, such as user registration, login, and authorization checks.
utils.py: Contains utility functions or helper methods used throughout the application.
tests/ directory:

test_routes.py: Includes unit tests for the API routes and functionality.
config.py file:

Holds configuration variables for your application, such as database connection details or secret keys.
requirements.txt file:

Lists the required dependencies for your project, including Flask and any other libraries you're using.
.gitignore file:

Specifies files and directories that should be ignored by Git when committing and pushing changes. Commonly includes the virtual environment folder (venv/) and any sensitive information like API keys or database credentials.
README.md file:

Contains documentation and instructions for setting up and using your debt tracking API.
run.py file:

Acts as the entry point of your application. It initializes the Flask app and runs it using the Flask development server.
