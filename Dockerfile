FROM python:3.10-slim-buster

# Update the default application repository sources list
RUN apt-get update

# Create a new user called "app"
RUN useradd app

# Set the working directory to /app/
WORKDIR /app

# Copy the poetry.lock and pyproject.toml files to the working directory
COPY poetry.lock pyproject.toml /app/

# Expose port 5000 for the Flask app to run on
EXPOSE 5000

# Set environment variables for the Flask app
ENV PYTHONUNBUFFERED=1 \
    PORT=5000

COPY . .

COPY ./pyproject.toml /app/pyproject.toml
COPY ./poetry.lock /app/poetry.lock
RUN pip install --no-cache-dir --upgrade poetry
RUN poetry config virtualenvs.create false
RUN poetry lock --no-update
RUN poetry install --no-dev --no-interaction --no-ansi

# Run gunicorn --config gunicorn_config.py run:app
CMD ["poetry", "run", "gunicorn", "--config", "gunicorn_config.py", "run:app"]
