# ppp_test_application

## Local development
Require: python 3.6 or above installed
### Create environment
Create and activate conda environment

`conda env create -f ppp_test_application.yaml`

`conda activate ppp_test_application `

### Make and execute migrations

`python3 manage.py makemigrations`

`python3 manage.py migrate`

### Create admin user

`python3 manage.py createsuperuser`

Create superuser to be able to utilize django admin backoffice

### Start server

python3 manage.py runserver 

