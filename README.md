# Event Application API

## Project Overview

The Event Application API serves as the backend for an event management application. It allows users to create, manage, and attend events. Key features include user authentication, event creation, ticket booking, notifications, and event analytics.

## Installation Instructions

### Prerequisites

Before setting up the project locally, ensure you have the following prerequisites installed:

- [Python](https://www.python.org/downloads/) (>=3.11.4)
- [Django](https://www.djangoproject.com/download/)
- [Django Rest Framework](https://www.django-rest-framework.org/#installation)
- A Database System (e.g., PostgreSQL, MySQL, SQLite) - [Django Database Installation](https://www.djangoproject.com/download/#database-installation)

### Installation Steps

1. Clone the repository:

        git clone https://github.com/hngx-org/Panthers-events-backend.git


2. Change into the parent directory:

        cd Panthers-events-backend


3. Change into the project directory:

        cd backend


4. Set up a virtual environment:

        py -m venv ENV


5. Activate your virtual environment:

        ENV\Scripts\activate


6. Install the Python dependencies:

        pip install -r requirements.txt


7. Configure the database settings in the `settings.py` file according to your chosen database system.


8. Apply migrations to create the database schema:

        python manage.py migrate


9. Create a superuser for administrative access:

        python manage.py createsuperuser


10. Start the development server: 
 ```
 python manage.py runserver
 ```

The API should now be running locally at [http://localhost:8000/](http://localhost:8000/).

## Usage Instructions


#### Event Management:

- /api/events/: Create, list, and search for events.
- /api/events/{event_id}/: Retrieve, update, or delete a specific event.
- /api/events/{event_id}/attendees/: Manage event attendees.

#### Group_Event Management:

- /api/groupevents/: Create, list, and search for events.
- /api/groupevents/{event_id}/: Retrieve, update, or delete a specific event.
- /api/groupevents/{event_id}/attendees/: Manage event attendees.

#### Group Management:

- /api/groups/: Create, list, and search for events.
- /api/groups/{event_id}/: Retrieve, update, or delete a specific event.
- /api/groups/{event_id}/attendees/: Manage event attendees.

#### User_Group Management:

- /api/usergroups/: Create, list, and search for events.
- /api/usergroups/{event_id}/: Retrieve, update, or delete a specific event.
- /api/usergroups/{event_id}/attendees/: Manage event attendees.


## Getting Started

To get started with the project, refer to the [Installation Instructions](#installation-instructions) and [Usage Instructions](#usage-instructions) sections. Familiarize yourself with the API endpoints by exploring the [API Documentation](documentation.md) provided.

## Configuration

Configuration details can be found in the project's `settings.py` file. Make sure to configure the required environment variables or configuration files as needed. Additionally, if any API keys or secrets are required, they should be mentioned in this section.

## Coding Standards

The project follows specific coding standards outlined in our [Coding Style Guide](#coding-standards). We use linting and code formatting tools to maintain code quality.

## API Documentation (if applicable)

You can access the API documentation [here](https://octopus-app-nax2o.ondigitalocean.app/) when the server is running. It provides comprehensive information on how to use the API endpoints.

## License Information

This project is open-source and is licensed under the [MIT License](LICENSE). For the full license text, please [click here](LICENSE).

## Contributors

We acknowledge and appreciate the contributions of the following individuals to this project:

- View the list of contributors in [Contributors.md](CONTRIBUTORS.md)

&copy; 2023 Team Panther Backend - HNG
