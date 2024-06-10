# Django INEC Results App

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Admin Interface](#admin-interface)
- [License](#license)

## Introduction
The Django INEC Results App is designed to manage and display election results at the ward level. It provides an admin interface to enter and view ward results, ensuring efficient data management and retrieval.

## Features
- Manage wards and their details.
- Enter and announce ward results.
- Admin interface for managing data.
- Secure and efficient data handling.

## Installation

### Prerequisites
- Python 3.x
- Django 3.x or later
- A database system (e.g., SQLite, MySQL)

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/wisteen/election-results.git
    cd election-results
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirments.txt
    ```

4. Apply database migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser to access the admin interface:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Access the application at `http://127.0.0.1:8000` and the admin interface at `http://127.0.0.1:8000/admin` or use the navigation.

8. Open your settings file and configure your database with your appropriate data base user details or you uncomment the SQLite database to get started imidiately if you dont have mysql installed 

## Usage

### Admin Interface
The admin interface allows you to manage wards and announced ward results and lot more you have access to all data and can manipulate and upload search and filter.

1. Go to the admin interface: `http://127.0.0.1:8000/admin`
2. Log in using the superuser credentials you created.
3. Add and manage Wards and Announced Ward Results through the interface.

## Models

### Ward
- `uniqueid`: Auto-increment primary key
- `ward_id`: Integer field for ward ID
- `ward_name`: CharField for ward name
- `lga`: ForeignKey to LGA model
- `ward_description`: TextField for ward description (optional)
- `entered_by_user`: CharField for the user who entered the data
- `date_entered`: CharField for the date entered
- `user_ip_address`: CharField for the user's IP address

### AnnouncedWardResults
- `result_id`: Auto-increment primary key
- `ward_name`: ForeignKey to Ward model
- `party_abbreviation`: CharField for party abbreviation
- `party_score`: Integer field for party score
- `entered_by_user`: CharField for the user who entered the data
- `date_entered`: CharField for the date entered (optional)
- `user_ip_address`: CharField for the user's IP address

## Admin Interface
The admin interface provides a convenient way to manage wards and their results.

### Accessing the Admin Interface
1. Navigate to `http://127.0.0.1:8000/admin`.
2. Log in with your superuser credentials.

### Managing Wards
1. Click on "Wards" to add, edit, or delete ward entries.
2. Enter the necessary details for each ward.

### Managing Announced Ward Results
1. Click on "Announced Ward Results" to add, edit, or delete ward results.
2. Enter the details of the results for each ward.

## NOTE: 
If you set up using sqlite for filed and drop down would be empty to click on the login button then sign in with  your superuser username and password then start inputing defualt data one by one and you will notcie that the home page is updataded 

check https://bincom.virtuallysafe.org to see how it works!
Admin login credentialz
username: wisteen
password: pass

## License
This project has no license 
