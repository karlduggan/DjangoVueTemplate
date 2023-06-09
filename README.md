# Project Name

Project Name is a web application built with the following:

- Django
- PostgreSQL
- Vue.js
- TailwindCSS

## Prerequisites

Before running this project, make sure you have the following installed:

- Docker: https://www.docker.com/get-started

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:

2. Build and start the Docker containers:

- `docker-compose build`
- `docker-compose up`

3. Wait for the Docker containers to build and start. You will see logs from both the Django backend and Vue.js frontend.

4. Once the containers are up and running, you can access the application:

- Django backend: http://localhost:8000
- Vue.js frontend: http://localhost:8080

5. To stop the containers, open a new terminal window, navigate to the project's root directory, and run the following command:

## Development

If you want to make changes to the project and develop locally, follow these steps:

1. Follow steps 1 and 2 from the "Getting Started" section to clone the repository and start the Docker containers.

2. Open the project in your preferred code editor.

3. Make your desired changes to the Django backend or Vue.js frontend.

4. The containers are configured to auto-reload whenever there are changes to the project files. So, you can view the updates in real-time as you save your changes.

5. If necessary, install additional Python packages for the Django backend by adding them to the `requirements.txt` file in the backend directory.

6. If necessary, install additional npm packages for the Vue.js frontend by running the following command in the frontend directory:

7. Test your changes locally by accessing the application at the provided URLs.

8. Once you're done with the development, stop the containers by running `docker-compose down` in the project's root directory.

## Additional Notes

- Superuser account detail:
    - Username: admin
    - Password: pass1234word
    - Email: user@admin.com
- The Django backend code can be found in the `backend` directory, and the Vue.js frontend code can be found in the `frontend` directory.
- The Docker configuration files (`Dockerfile` and `docker-compose.yml`) are provided in the project's root directory.
- Make sure to update the Django and Vue.js project names and configurations according to your project's specifics.

## DOCKER SOLUTIONS

1. When building docker it sometimes doesn't create the node modules directory, to resolve this navigate to the frontend directory and `npm install` in the terminal, this will create the node_modules directory

2. Use `docker exec -it` for making changes to django and ensure that the container is running first, for example:
- `python manage.py migrate` = `docker exec -it <container_id> python manage.py migrate`
- `python manage.py makemigrations` = `docker exec -it <container_id> python manage.py makemigrations`
- `python manage.py createsuperuser` = `docker exec -it <container_id> python manage.py createsuperuser`


Enjoy!

## Resources

Setting up Django with PostgreSQL
https://www.youtube.com/watch?v=610jg8bK0I8
Django & Postgres with Docker Best Practices
https://www.youtube.com/watch?v=4wdNx2j1j-w
