deploy:
	mkdir ./postgres/database
	docker-compose -f docker-compose.yml up -d --build
	ping 8.8.8.8 -c 10
	cat ./database.dump | docker-compose exec -T postgres psql -U postgres
stop:
	docker-compose stop
start:
	docker-compose start
dump_db:
	docker-compose exec postgres pg_dump -U postgres > ./database.dump
restore_db:
	cat ./database.dump | docker-compose exec -T postgres psql -U postgres
psql:
	docker-compose exec postgres psql -U postgres
