# Use the same base image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy your test files and any necessary application code to the container
COPY ./tests /code/tests  
COPY ./sas_running /code/sas_running  
COPY ./main.py /code/main.py
# Command to run tests
# Adjust this command according to your test structure and requirements
CMD ["python3", "-m", "pytest"]