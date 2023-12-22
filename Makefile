
publish:
	$ poetry run python freeze.py
	$ poetry run ghp-import -m "Update site" build
	$ git push -f origin gh-pages:main
	$ git push origin write:write

dev_server:
	$ FLASK_DEBUG=true FLASK_ENV=development poetry run flask run -p 5100