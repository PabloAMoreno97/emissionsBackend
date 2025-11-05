# Emissions App – Backend

This repository contains the backend API for the **Emissions App**, developed using **Python** and **Django REST Framework**.

It provides RESTful endpoints for managing and retrieving emissions data by country, activity, and emission type.
The API is designed to support the Angular-based frontend and can be run locally or in a Docker container.

## 1. Clone the Repository
First, clone the repository from Github using one of the next commands:

#### using HTTPS connection:
```
git clone https://github.com/PabloAMoreno97/emissionsBackend.git
```

#### Using SSH connection:
```
git clone git@github.com:PabloAMoreno97/emissionsBackend.git
```

Then navigate into the project directory:
```
cd emissionsBackend
```

## 2. Running the Application with Django Locally

### 2.1 Installation and Setup (Windows):
Create a virtual environment:
```
python -m venv .venv
```

Activate the environment:
```
.venv/Scripts/activate
```

Install the project dependencies:
```
pip install -r "requirements.txt"
```

Apply migrations to create the local SQLite database:
```
python manage.py migrate
```

### 2.2 Starting the Development Server
To start the application locally, navigate to the project directory in your terminal and run:

```
python manage.py runserver
```

Once the server starts, open your browser and go to:

*http://localhost:8000/api/emissions/*


The application will automatically reload when application files are modified.

### 2.3 Stopping the Development Server
To stop the Django development server, use the following keyboard shortcut in the same terminal window:
```
Ctrl + C
```

## 3. Running the Application with Docker
You can also build and run the backend inside a Docker container.

### 3.1 Building the Docker Image
From the root project directory, build the image:
```
docker build -t emissions-backend .
```

### 3.2 Running the Docker Container
Start a new container:
```
docker run -d --name emissions-backend -p 8000:8000 emissions-backend
```

Once running, the API will be accessible at:

*http://localhost:8000/api/emissions/*


### 3.3 Stopping and Removing the Container
To stop the container:
```
docker stop emissions-backend
```

To remove the container:
```
docker rm emissions-backend
```

To remove the image:
```
docker image rm emissions-backend
```

## 4. Running Unit Tests
Before running the unit tests, follow the **step 2.1** to install the dependencies.

To execute the tests, run:
```
python manage.py test
```

This command runs Django’s built-in test suite and displays the results in the terminal.

## 5. Project Structure Overview
Key directories and files:

```
emissionsBackend/
 ├── config/                 # Django project configuration and settings
 ├── core/                   # Main application with models, views, and serializers
 ├── manage.py               # Django management utility
 └── requirements.txt        # Python dependencies
```

## 6. Pre-requisites
Before running or building the project, ensure that you have the following installed:

- **Python** (version 3.12 or higher)
- **pip** (Python package manager)
- **Docker** *(optional, for containerized execution)*

## 7. API Overview

### Emissions
|Endpoint | Method | Description |
| ------------| ------ | -------- |
/api/emissions/	| GET | Retrieves all emission records |
/api/emissions/\<id>/ | GET | Retrieves details of a specific emission |
/api/emissions/ | POST | Creates a new emission entry |
/api/emissions/\<id>/ | PATCH | Partially updates an existing emission entry |
/api/emissions/\<id>/ | PUT | Updates an existing emission entry |
/api/emissions/\<id>/ | DELETE | Deletes an emission entry |

### Countries
|Endpoint | Method | Description |
| ------------| ------ | -------- |
/api/countries/	| GET | Retrieves all country records |
/api/countries/\<id>/ | GET | Retrieves details of a specific country |
/api/countries/	| POST | Creates a new country entry |
/api/countries/\<id>/ | PATCH | Partially updates an existing country entry |
/api/countries/\<id>/ | PUT | Updates an existing country entry |
/api/countries/\<id>/ | DELETE | Deletes a country entry |

### Emission Type
|Endpoint | Method | Description |
| ------------| ------ | -------- |
/api/emission_types/ | GET | Retrieves all emission type records |
/api/emission_types/\<id>/ | GET | Retrieves details of a specific emission type |
/api/emission_types/ | POST | Creates a new emission type entry |
/api/emission_types/\<id>/ | PATCH | Partially updates an existing emission type entry |
/api/emission_types/\<id>/ | PUT | Updates an existing emission type entry |
/api/emission_types/\<id>/ | DELETE | Deletes an emission type entry |

### Activities
|Endpoint | Method | Description |
| ------------| ------ | -------- |
/api/activities/ | GET | Retrieves all activity records |
/api/activities/\<id>/ | GET | Retrieves details of a specific activity |
/api/activities/ | POST | Creates a new activity entry |
/api/activities/\<id>/ | PATCH | Partially updates an existing activity entry |
/api/activities/\<id>/ | PUT | Updates an existing activity entry |
/api/activities/\<id>/ | DELETE | Deletes an activity entry |