# Capstone Project
## EE Department
* This project is the capstone project of the Full Stack Developer Nano Degree by Udacity. The goal of this project is to deploy a Flask application to Heroku with Role-Based Access Control(RBAC) using Auth0, a third-party authentication system.

* I decided to implement a RESTful for  EE-Department application that enables users to create/manage sheets and subjects. The motivation behind this project is for me to apply all skills that I have learned so far in the Udacity's Full Stack Developer Nano Degree course, including architecturing relational database, modeling data objects with SQLAlchemy, writing, testing and documenting a Flask API, integrating third-party authentication system, and successfully deploying an application. 
* This project is coded in Python3 and is styled to PEP 8 Style Guide.

## Getting Started
### Pre-requisites and Local Development
* You should already have Python3, pip and node installed on your local machines
* To create a virtual environment on MacOS, run:
* ```python3 -m venv env```
* To activate the virtual environment, run:
* ```source env/bin/activate```
## About the Stack
### Backend
* On MacOS, to set up all the dependencies, run:
* ```pip install requirements.txt```
* To run the application on your local machine, run:
* ```python3 app.py```
* The application is hosted on https://ee-department.herokuapp.com and can also be run locally at http://127.0.0.1:5000/ .
* The PostgreSQL database is hosted on Heroku. If you want to run locally using your local databse, you can modify the following fields in the models.py file:
* ```database_name =<your_database_name>, database_path = <your_database_path```

### Frontend
* Work in Progress
### Authentication Set Up
* Tokens can be found in the setup.sh file.
### Testing
* To run the tests locally, you need to have PostgreSQL installed on your local machines already.
* To set up a test database, replace the following fields on the test_app.py file:
* To run the tests, run: 
* ```python3 test_app.py ```
## API Reference
### Getting Started
* Base URL: This app is hosted on: https://ee-department.herokuapp.com, or it can be run locally on http://127.0.0.1:5000/
* Authentication: This version of the application requires authentication for all endpoints

### Error Handlin
* Errors are returned as JSON objects in the following format:
```
{
  "success": False,
   "error": 400,
   "message": "Bad Request"
}
```
* The API will return these error types when requests fail:
- 400: Bad Request
- 404: Not Found
- 422: Unprocessable
- 405: Method Not Allowed
- 500: Internal Server Error

* If authentication is required, these error types will be returned when requests fail:
- 401 : Errors regarding authorization headers or token (i.e: "Token expired")
- 403: Permission not found
- 400: Invalid header
### Roles and Permissions
* There are 3 roles:
- Casting Assistant: Can view sheets and subjects
- Casting Director: Can view sheets and subjects, add from the database, and modify sheets or subjects
- Producer: Have all permissions

### Endpoints
#### GET /subjects (Casting Assistant, Casting Director, Producer)
* General: Returns a list of all subjects objects and success value
* Sample:
```
{
  "subjects": [
    {
      "name": "Mathematics"
    },
    {
      "name": "Physics"
    }
  ],
  "success": true
}
```
#### GET /sheets (Casting Assistant, Casting Director, Producer)
* General: Returns a list of all sheets objects and success value
* Sample:
```
{
  "sheets": [
    {
      "release date": "2020-02-11",
      "title": "EE434"
    },
    {
      "release date": "2019-12-10",
      "title": "EE532"
    }
  ],
  "success": true
}
```

#### POST /subjects (Casting Director, Producer)
* General: Creates a new subject using JSON request parameter and returns success value, newly created subject
* Sample: Response for a request with following body {"name": "Physics"} and the appropriate header: 

```
{
  "new subject added": {
    "name": "Physics"
  },
  "success": true
}
```
#### POST /sheets (Producer)
* General: Creates a new sheets using JSON request parameters and returns success value, newly created sheet
* Sample: Response for a request with following body {"title": "EE302", "release_date": "2020-01-03"} and the appropriate header:
```
{
  "new sheet added": {
    "release_date": "2020-01-03",
    "title": "EE302"
  },
  "success": true
}
```
#### DELETE /subjects/<<int:id>> (Casting Director, Producer)
* General: Deletes a subject from the database by id and returns success value and id of the deleted subject
* Sample: Response for a request to delete an subject with id=2 and the appropriate header:
```
{
  "deleted": 2,
  "success": true
}
```
#### DELETE /sheets/<<int:id>> (Producer)
* General: Deletes a sheet from the database by id, returns success value and id of the deleted sheet
* Sample: Response for a request to delete a sheet with id=2 and the appropriate header:
```
{
  "deleted": 2,
  "success": true
}
```
#### PATCH /subject/<<int:id>> (Casting Director, Producer)
* General: Modifies an subject by id using JSON request parameters and returns success value and id of the modified subject
* Sample: Response for a request to modify a subject with id=3, with the following body {"name": "Physics"} and the appropriate header:
```
{
  "success": true,
  "updated": 3
}
```
#### PATCH /sheet/<<int:id>> (Casting Director, Producer)
* General: Modifies a sheet by id using JSON request parameters; returns success value and id of the modified sheet
* Sample: Response for a request to modify a sheet with id=3, with the following body{"title": "EE452", "release_date": "2020-01-02"} and the appropriate header:
```
{
  "success": true,
  "updated": 3
}
```
## Authors
* Abdelfattah
## Acknowledgements
* I would like to thank Udacity for the idea suggestion of this project
