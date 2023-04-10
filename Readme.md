# Django Tutorials

## 1. Abstract Model 

### API : 

URL PATH : abstract_models/


## Database

### Backup
 
pg_dump -U postgres ygpay_db_main -h localhost > ygpay_db_main_copy_2.sql


psql -U postgres

create database youpay_

### Restore
 
pg_dump -U postgres youpay_db_1 -h localhost < ygpay_db_main_copy_2.sql


python manage.py dumpdata > db.json


python manage.py loaddata "path/to/fixture/file"


### Clone database cmd

psql -U postgres   

syntax : create database [NEW_DATABASE] with template [DATABASE_TO_COPY] owner [OWNER_USERNAME];

postgres=# create database ygpay_db_main_copy with template ygpay_db_main owner postgres;



<!-- Celery -->


### using RabitMQ

`docker run -d -p 5672:5672 rabbitmq`

`pip install celery`

`source venv/bin/activate`

### Run Celery Worker Server

`celery -A tasks worker --loglevel=INFO`


```

python manage.py shell

from django_tutorials.tasks import add

add.delay(2,4)


```