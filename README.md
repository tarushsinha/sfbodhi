# sfbodhi

#######
How to Run:
#python3 -m venv venv
#source venv/bin/activate
#pip install -r requirements.txt
#cd sfbodhi
#python manage.py migrate
#python manage.py runserver
#######


#######
if any updates to table schema (regular runs)
#python manage.py makemigrations
#python manage.py migrate
#python manage.py runserver
#######


#######
How to clean/reset DB
#rm db.sqlite3
#find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
#find . -path "*/migrations/*.pyc" -delete
#python manage.py makemigrations
#python manage.py migrate


### Acknowledgements

This project uses the [Pyvis](https://github.com/WestHealth/pyvis) library for interactive network graph visualization.  
Pyvis is licensed under the BSD 3-Clause License. See [THIRD_PARTY_LICENSE/pyvis.txt](THIRD_PARTY_LICENSE/pyvis.txt) for details.
