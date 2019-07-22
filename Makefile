_django_user = django
_execc = docker-compose exec
_django_execc = docker-compose exec --user=$(_django_user) app

pip_install:
	$(_execc) --user=root app pip3 install -r requirements.txt

test:
	$(_django_execc) python manage.py test
