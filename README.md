# payroll-software
Project for CSCI-490

### Design Pattern
MVC (Model, View, Controller)

Model: This will handle the application's data logic, such as employee hours, wages, tax rates, and administrator information. This layer would manage how the data is stored, retrieved, and manipulated, likely interfacing with a SQL database.

View: This is responsible for presenting the data to the user, whether it's the employee entering hours or the admin managing them. This would likely include web pages or API responses since our application is full stack.

Controller: This acts as the intermediary between the model and view, handling user input, manipulating data in the model, and determining which view to display.

### Folder Structure
project_root/
│
├── app/                # Core application code (models, views, controllers)
│   ├── controllers/    # Contains controller logic
│   ├── models/         # Contains business logic and database models
│   ├── views/          # Contains UI templates (HTML, JSON, etc.)
│   ├── static/         # Static files (CSS, JavaScript, images)
│   ├── templates/      # Templates for HTML views (if using a web framework like Flask)
│   └── __init__.py     # Makes `app/` a Python package
│
├── migrations/         # Database migrations (if using a framework like Flask with SQLAlchemy)
│
├── tests/              # Test cases for the app
│   └── test_models.py  # Unit tests for models
│   └── test_views.py   # Unit tests for views
│   └── test_controllers.py # Unit tests for controllers
│
├── config.py           # Configuration settings (database URI, environment variables)
├── requirements.txt    # List of dependencies
├── .env                # Environment variables (e.g., database credentials, secrets)
├── README.md           # Documentation about the project
└── run.py              # Entry point to run the application


Here’s a breakdown of the different folders and files:

`app/`: Contains all the core logic

`controllers/`: Contains the logic that connects user actions (HTTP requests, user input, etc.) to the application’s models and views. These scripts will process the requests from the user and call the appropriate functions in the models or generate responses in the views.
Example: employee_controller.py could handle creating, updating, and deleting employees.
`models/`: The models folder holds all the classes that represent your data and business logic. For example, you would define your Employee model here, as well as any database interaction.
Example: employee_model.py could represent the data structure for employees and methods to interact with the database (SQL queries).

`views/`: The views folder contains the UI components or response formatting. If your app is web-based, these would be HTML templates, JSON responses, or other formats the front end would need.
Example: employee_view.py would contain functions to render employee data, like rendering a webpage for employee input or outputting a JSON response for an API.

`static/`: For web apps, this would store static assets like CSS, JavaScript, and images.

`templates/`: If you're using a web framework like Flask or Django, this folder stores HTML templates for the front end.
migrations/: If you’re using a database framework like SQLAlchemy or Flask-Migrate, this folder will handle database migration scripts.

`tests/`: All your test cases will go here, allowing you to unit test models, views, and controllers.

`config.py`: This file will hold configuration settings for your app, like database connection settings, API keys, and environment-specific variables.

`requirements.txt`: A list of external Python dependencies needed for your project, which you can generate using pip freeze.

`.env`: This file stores environment variables (e.g., database credentials) that are loaded at runtime. Use something like python-dotenv to manage these in your app.

`run.py`: This will be the entry point for starting your application. For example, if you're using Flask, it would initialize the Flask app.
