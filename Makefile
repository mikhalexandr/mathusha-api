requirementsRemove:
	pip freeze > requirements.txt
	pip uninstall -y -r requirements.txt

requirementsAdd:
	pip freeze > requirements.txt

requirementsInstall:
	pip install -r requirements.txt

keycloack:
	docker run -p 8080:8080 -e KEYCLOAK_ADMIN=mikhalexandr -e KEYCLOAK_ADMIN_PASSWORD=mikhalexandr quay.io/keycloak/keycloak:24.0.4 start-dev
