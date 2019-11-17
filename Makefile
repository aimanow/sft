# Makefile

build:
	echo "Set chmod to directories"
	echo "Building all containers:"
	sudo sysctl -w vm.max_map_count=262144
	sudo docker-compose build

start:
	echo "Starting all containers:"
	sudo docker-compose up -d

stop:
	echo "Stopping all containers:"
	sudo docker-compose down -v

restart:
	echo "Restarting all containers:"
	make stop
	make start
	make logs

logs:
	sudo docker-compose logs -f

console:
	sudo docker exec -it backendapp /bin/sh

list:
	sudo docker ps

rebuilt:
	make stop
	make build
	make start

push:
	git add *
	git commit -m "Fixes"
	git push
