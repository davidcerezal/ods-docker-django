build:
	docker-compose build

up:
	docker-compose up -d

up-non-daemon:
	docker-compose up

start:
	docker-compose start

stop:
	docker-compose stop

restart:
	docker-compose stop && docker-compose start

shell-nginx:
	docker exec -ti nz01 /bin/sh

shell-web:
	docker exec -ti dz01 /bin/sh

shell-db:
	docker exec -ti pz01 /bin/sh

log-nginx:
	docker-compose logs nginx  

log-web:
	docker-compose logs web  

log-db:
	docker-compose logs db


collectstatic:
	docker exec dz01 /bin/sh -c "python manage.py collectstatic --noinput"

import:
	docker exec dz01 /bin/sh -c "python manage.py ImportApiFootBallOds"

delete:
	docker exec dz01 /bin/sh -c "python manage.py deleteExpiredBetsAndSurebets"

calculate:
	docker exec dz01 /bin/sh -c "python manage.py calculateSureBets"

#-------PRODUCTION
prod-build:
	docker-compose  -f docker-compose.prod.yml build

prod-up:
	docker-compose  -f docker-compose.prod.yml up -d

deploy:
	docker-compose -f docker-compose.prod.yml down && docker-compose -f docker-compose.prod.yml build --no-cache && docker-compose -f docker-compose.prod.yml up -d

prod-log-nginx:
	docker-compose -f docker-compose.prod.yml logs nginx

prod-log-web:
	docker-compose -f docker-compose.prod.yml logs web

prod-log-db:
	docker-compose -f docker-compose.prod.yml logs db

