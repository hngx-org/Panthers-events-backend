<!DOCTYPE html>
<html>
<head>
    <title>Event Application API</title>
</head>
<body>
    <h1>Event Application API</h1>

    <h2>Project Overview</h2>

    <p>The Event Application API serves as the backend for an event management application. It allows users to create, manage, and attend events. Key features include user authentication, event creation, ticket booking, notifications, and event analytics.</p>

    <br/>

    <h2>Installation Instructions</h2>

    <h3>Prerequisites</h3>

    <h6>Before setting up the project locally, ensure you have the following prerequisites installed:</h6>

    <ul>
        <li><a href="https://www.python.org/downloads/">Python</a> (>=3.11.4)</li>

        <li><a href="https://www.djangoproject.com/download/">Django</a></li>

        <li><a href="https://www.django-rest-framework.org/#installation">Django Rest Framework</a></li>

        <li>A Database System (e.g., PostgreSQL, MySQL, SQLite) - <a href="https://www.djangoproject.com/download/#database-installation">Django Database Installation</a></li>
    </ul>

    <br/>

    <h3>Installation Steps</h3>

    <ol>

        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/hngx-org/Panthers-events-backend.git</code></pre>
    
    

    
        <li>Change into the parent directory:</li>
        <pre><code>cd Panthers-events-backend</code></pre>
    
    

    
        <li>Change into the project directory:</li>
        <pre><code>cd backend</code></pre>
    
    

    
        <li>Set up a virtual environment:</li>
        <pre><code>py -m venv ENV</code></pre>
    
    

    
        <li>Activate your virtual environment:</li>
        <pre><code>ENV\Scripts\activate</code></pre>
    
    

    
        <li>Install the Python dependencies:</li>
        <pre><code>pip install -r requirements.txt</code></pre>
    
    

    
        <li>Configure the database settings in the settings.py file according to your chosen database system.</li>
    

    
        <li>Apply migrations to create the database schema:</li>
        <pre><code>python manage.py migrate</code></pre>
    
    

    
        <li>Create a superuser for administrative access:</li>
        <pre><code>python manage.py createsuperuser</code></pre>
    
    

    
        <li>Start the development server:</li>
        <pre><code>python manage.py runserver</code></pre>

    </ol>
    

    <p>The API should now be running locally at <a href="http://localhost:8000/">http://localhost:8000/</a>.</p>

    <br/>

    <h2>Usage Instructions</h2>

    <h3>Authentication</h3>

    <p>To access most endpoints of the API, you need to authenticate. Use the Token-based authentication method by making a POST request to <code>/api/token/</code> with your username and password.</p>

    <p>User Authentication:</p>
    <ul>
        <li>/api/token/: Obtain an authentication token.</li>
    </ul>

    <p>Event Management:</p>
    <ul>
        <li>/api/events/: Create, list, and search for events.</li>

        <li>/api/events/{event_id}/: Retrieve, update, or delete a specific event.</li>

        <li>/api/events/{event_id}/attendees/: Manage event attendees.</li>
    </ul>

    <p>Ticket Booking:</p>
    <ul>
        <li>/api/tickets/: Book and manage event tickets.</li>

        <li>/api/tickets/{ticket_id}/: Retrieve, update, or cancel a specific ticket.</li>
    </ul>

    <p>Notifications:</p>
    <ul>
        <li>/api/notifications/: Get event notifications.</li>

        <li>/api/notifications/{notification_id}/: Mark a notification as read.</li>
    </ul>

    <p>Analytics:</p>
    <ul>
        <li>/api/analytics/: Retrieve event analytics data.</li>
    </ul>

    <br/>

    <h2>Getting Started</h2>

    <p>To get started with the project, refer to the <a href="#installation-instructions">Installation Instructions</a> and <a href="#usage-instructions">Usage Instructions</a> sections. Familiarize yourself with the API endpoints by exploring the <a href="#api-documentation">API Documentation</a> provided.</p>

    <br/>

    <h2>Configuration</h2>

    <p>Configuration details can be found in the project's <code>settings.py</code> file. Make sure to configure the required environment variables or configuration files as needed. Additionally, if any API keys or secrets are required, they should be mentioned in this section.</p>

    <br/>

    <h2>Contributing Guidelines</h2>

    <p>We welcome contributions from the community. Please follow our <a href="#contributing-guidelines">Contributing Guidelines</a> for information on how to contribute to the project. You can submit bug reports, feature requests, or pull requests following the outlined process.</p>

    <br/>

    <h2>Coding Standards</h2>

    <p>The project follows specific coding standards outlined in our <a href="#coding-standards">Coding Style Guide</a>. We use linting and code formatting tools to maintain code quality.</p>

    <br/>

    <h2>Testing and Quality Assurance</h2>

    <p>To ensure code quality, follow the instructions in the <a href="#testing-and-quality-assurance">Testing Guidelines</a> for running tests and quality checks on the codebase. The project uses a testing framework, and details on the testing tools are provided.</p>

    <br/>

    <h2>Deployment Instructions (if applicable)</h2>

    <p>For deployment to a production environment, please refer to our <a href="#deployment-instructions-if-applicable">Deployment Instructions</a>. This document includes step-by-step instructions and configuration details for deploying the project.</p>

    <br/>

    <h2>API Documentation (if applicable)</h2>

    <p>You can access the API documentation <a href="#api-documentation">here</a> when the server is running. It provides comprehensive information on how to use the API endpoints.</p>

    <br/>

    <h2>License Information</h2>

    <p>This project is open-source and is licensed under the <a href="LICENSE">MIT License</a>. For the full license text, please <a href="LICENSE">click here</a>.</p>

    <br/>

    <h2>Contributors</h2>

    <p>We acknowledge and appreciate the contributions of the following individuals to this project:</p>

    <ul>
        <li><a href="mailto:your.email@example.com">Our Names</a> - GitHub Profile: <a href="https://github.com/your-username">Our GitHub Profiles</a></li>
    </ul>

    <br/>

    <h2>Project Roadmap (Optional)</h2>
    <p>Our project roadmap outlines future plans and enhancements for the project. It serves as a guide for potential contributors and collaborators. You can find the roadmap in the <a href="ROADMAP.md">ROADMAP.md</a> file.</p>

    <footer>
        <p>&copy; 2023 Team Panther Backend - HNG</p>
    </footer>
</body>
</html>