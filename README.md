# newsroom_project

Install all the dependencies from the requirements.txt file by running the following docker command: `docker-compose up -d --build`

to start the project you have to migrate with the following command: `docker-compose exec web python manage.py migrate`

Start the project by running the following command: `docker-compose up` or `docker-compose up -d`

For rest api you should go on following urls: `http://localhost:8000/api/articles/articles` or `http://localhost:8000/api/blocks/blocks`

