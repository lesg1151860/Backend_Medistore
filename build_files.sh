pip install -r requirements.txt
python MediStore/manage.py migrate
python MediStore/manage.py collectstatic --noinput