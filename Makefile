build:
	docker build -f cristian -t cristian:3.0.0 .

test:
	pytest -q

run:
	docker run --rm -p 1002:80 cristian:3.0.0
