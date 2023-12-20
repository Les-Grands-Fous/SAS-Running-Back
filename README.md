# SAS Running Tracker 🏃‍♂️💨

## Overview

This project is a FastAPI-based web application designed exclusively for employees of SAS Company to track their daily running distances. It includes a login/register page and a ranking system to showcase the individuals who have run the most. Lace up your running shoes and let's get started! 🏅👟

## Technologies Used

- **Backend Framework:** [FastAPI](https://fastapi.tiangolo.com/) 🚀
- **Database:** [PostgreSQL](https://www.postgresql.org/) 🗃️
- **Object-Relational Mapping:** [SQLModel](https://sqlmodel.tiangolo.com/) 🗄️
- **Database Migrations:** [Alembic](https://alembic.sqlalchemy.org/en/latest/) 🔄
- **Dependency Management:** [Poetry](https://python-poetry.org/) 📦
- **Containerization:** [Docker](https://www.docker.com/) 🐳

## Project Structure

```plaintext
sas_running_back/
|-- sas_running/                 # FastAPI code source
|   |-- main.py
|-- README.md                    # Project documentation
|-- pyproject.toml               # Poetry configuration (We will add it later)
|-- alembic/                     # Alembic configuration and migrations (We will add it later)
|-- docker-compose.yml           # Docker Compose configuration (We will add it later)
|-- Dockerfile                   # Docker configuration (We will add it later)
|-- requirements.txt             # Prod Requirements configuration
|-- requirements-dev.txt         # Dev Requirements configuration
|-- main.py                      # Python file that we will execute to launch the API
|-- .env                         # Env file that we will store all the secrets that the API needs to run
```

## Setup

1. **Clone the Repository:**

    ```bash
    git clone git@github.com:Souhib/sas-running-back.git
    cd sas-running-back
    ```

    📥 This command clones the project repository from GitHub to your local machine and navigates into the project directory.

2. **Install Dependencies:**

    ```bash
    poetry install
    ```

    📦 Poetry is a dependency management tool for Python. Running poetry install installs all the project dependencies specified in the pyproject.toml file.

    Alternative: Using `requirements.txt`

    ```bash
    pip install -r requirements.txt
    ```

    📜 If you prefer using pip and a traditional requirements.txt file, you can install the dependencies this way. The requirements.txt file contains a list of Python packages and their versions.

4. **Run the FastAPI Application:**

    Using Poetry:

    ```bash
    poetry run uvicorn main:app --reload
    ```

    ▶️ This command starts the FastAPI application. The --reload option enables automatic code reloading during development. After running this command, the API will be accessible at http://127.0.0.1:8000.

    Alternative: Using `Python`:

    ```bash
    uvicorn main:app --reload
    ```
    or
    
    ```bash
    python main.py
    ```

## Feature Development with GitHub Pull Requests

To contribute new features or enhancements to the project, follow these steps:

1. **Create a New Branch:**

    ```bash
    git branch feature-branch-name # Create the branch "feature-branch-name"
    git checkout feature-branch-name # Move to the branch "feature-branch-name"
    ```

2. **Work on your branch:**

    Add your work on your branch by pushing into it as always :

    ```bash
    git add --all
    git commit -m "WIP"
    git push origin feature-branch-name
    ```

2. **Create a Pull Request:**

    Open a pull request on GitHub from your feature branch to the dev branch. This allows your changes to be reviewed and merged into the development branch.
    Make sure to make it `draft pull request` and when you're done working on it and want a review, make it a normal pull request 

## Additional Notes

Production Setup: For a `production` environment with `Docker` and `PostgreSQL`, additional steps and configurations are needed. Refer to the project structure for placeholders (pyproject.toml, alembic/, docker-compose.yml, Dockerfile, .env) that will be added later for a complete production setup.
