
publish:
	$ ./publish.sh

dev_server:
	$ source .env
	$ FLASK_ENV=development poetry run flask run -p 5100