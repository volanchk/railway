web: python manage.py createsuperuser --noinput --username volanchk --email bestbook@gmail.com 
  && python manage.py makemigrations 
  && python manage.py migrate 
  && python manage.py collectstatic --no-input 
  && gunicorn bestbook.wsgi
