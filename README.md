# Deployment of ML Models

- In this README, it is explained how to set up the project environment, what the project packages are for, and what type of data returns the modules are.

## Fresh Install

----------------------------------------------------------------
- Clone repository
  - `https://github.com/anilsdemir/deploying-ml-models.git`
----------------------------------------------------------------
- Install virtualenv
  - `pip install virtualenv`
- Create a virtual environment and activate it
  - `virtualenv --python=/usr/bin/python3.9 deploying-ml-models-venv`
  - `source deploying-ml-models-venv/bin/activate`
----------------------------------------------------------------
- Install pip-tools: `pip install pip-tools`
- Change directory to `requirements/`
  - Install required packages: `pip install -r requirements.txt`
- **[Optional]** If you want to change versions of libraries or add new libraries, after modifying requirements.in, run this code to generate requirements.txt
  - Generate requirements.txt: `pip-compile requirements.in`
- Install pre-commit hooks: `pre-commit install`
----------------------------------------------------------------

## Run Project
## Running the Project
- Change the directory to `src/`
- Run this code **[will be updated]**