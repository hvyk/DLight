## Install pipenv (Optional)

``` basg
pipenv install django==2.2.0
pipenv install djangorestframework
pipenv shell
```

## Requirements:
```
django = "==2.2.0"
djangorestframework = "*"
```

## Running
```bash
./cleandb.sh # makemigrations, and migrate
python manage.py runserver
```

## Testing
Import the Postman collection into Postman and run the entire collection.  It should pass all the required tests and create the Flavours, Containers, and Orders in the database