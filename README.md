Product Crud
===
You must have latest/reliable version of python installed on your machine

You can follow this [Video](https://drive.google.com/file/d/1cJT1GLP_INRahFL63fy2BnvMkbmagSrL/view?usp=sharing)
or Setup steps below to run the project

Setup
===
1. Clone the repo
```bash
git clone https://github.com/MoinulNabil/Crud.git
cd Crud
```

2. Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows:
```bash
venv\Scripts\activate
```

Linux
```bash
source venv/bin/activate
```

3. Run the Project

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata db.json # populate database with initial data
python manage.py runserver
```

Usage
===
The devlopment server runs on loclhost:8000. The api's are as follows:

Endpoints
```bash
POST /items/ # Creates new item
GET /items/ # List all items
GET /items/{id} # Get details of a specific item
PUT /items/{id} # Update details of a specific item
DELETE /items/{id} # Delete a specific item
```

Full Path
```bash
localhost:8000/items/
localhost:8000/items/
localhost:8000/items/{id}
localhost:8000/items/{id}
localhost/items/{id}
```

Api Doc
===
Go to http://localhost:8000/api/doc/ for the api listing

Postman
===
Collection file > postman_collection.json

Technology Used
===
* Python
* Django Rest Framework
* Sqlite3
