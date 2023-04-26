## Django-Rest

This is a Django project that provides a backend structure for managing clients, artists, and works. It also includes REST API endpoints for listing works, artists, and creating works.

### Getting Started
To run this project locally, please follow these steps:

1. Clone this repository to your local machine
2. Navigate to the project root directory in the command line
3. Create a virtual environment using the following command:

   `python -m venv myvenv`

4. Activate the virtual environment using the following command:

   `myvenv\Scripts\activate`

5. Install the project dependencies using the following command:

   `pip install -r requirements.txt`

6. Run the project server using the following command:

   `python manage.py runserver`

7. Navigate to http://localhost:8000 in your web browser to access the project.

### Database Setup
This project uses the default SQLite database that comes with Django. To set up the database, run the following command:

   `python manage.py migrate`

### Admin Panel
The Django admin panel is available at http://localhost:8000/admin. You can use it to manage the client, artist, and work models in the project.

### Test Admin
```
username: admin
password: admin
```
If this does not work then try creating a super user with
```
python manage.py createsuperuser
```
and check the tables after migration
### API Endpoints
This project includes the following REST API endpoints:
#### List Works
```
GET /api/works/
```
Returns a list of all works in the system.

Filter by Work type
```
GET /api/works/?work_type={work_type}
```
Returns a list of works filtered by the specified work type.

Search by Artist artist_name
```
GET /api/works/?artist={artist_name}
```
Returns a list of works that are associated with the specified artist.

Create Work
```
POST /api/works/create/
```
Creates a new work in the system. The request body should contain the following fields:
```
link (string): The link to the work
work_type (string): The type of work (either "Youtube", "Instagram", or "Other")
artists (array): An array of artist ids associated with this work

```
List Artists
```
GET /api/artists/
```
Returns a list of all artists in the system.

Create Client
```
POST /api/register/
```
Creates a new client in the system.
The request body should contain the following fields:
```
username (string): The client's username
password (string): The client's password
```

### Links to test
You can test the API endpoints using the following URLs:
```

http://127.0.0.1:8000/api/works
http://127.0.0.1:8000/api/works?artist=[Artist Name]
http://127.0.0.1:8000/api/works?work_type=Youtube
http://127.0.0.1:8000/api/works/create
```


