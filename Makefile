pull:
	git checkout main && git pull
run:
	python manage.py runserver 8005
migrate:
	python manage.py makemigrations && python manage.py migrate
activate:
	source env/bin/activate
test:
	export DJANGO_SETTINGS_MODULE=mysite.settings && pytest -vv
push:
	git push
