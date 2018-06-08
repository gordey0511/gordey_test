rm -R static/static_prod
python3 manage.py collectstatic
python3 manage.py runserver localhost:8080
