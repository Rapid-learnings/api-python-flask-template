# <Project Name> API Service

## Overview

<< Project Overview >>

## Features

- **Swagger Documentation**: Explore the API using the Swagger UI.
- **Feature 1**: Feature 1 description.
- **Feature 2**: Feature 2 description.

## Requirements

- Python 3.10 or higher
- [Poetry](https://python-poetry.org/) for dependency management

## Installation

1. **Clone the Repository**:

   ```shell
   git clone <<repo-url>>
   cd api-python-flask-template
   ```

2. **Install Poetry**:

   Poetry is a tool for dependency management and packaging in Python. To install Poetry, follow the instructions on the [official website](https://python-poetry.org/docs/).

3. **Install Dependencies with Poetry**:

   Run the following command to install project dependencies:

   ```shell
   poetry install
   ```

4. **Environment Variables**:

   - Create a `.env` file based on the `.env.example`.

     ```shell
     cp .env.example .env
     ```

   - Fill in the necessary details like `ENV`, `HOST`, and `PORT`.

## Usage

1. **Activate the Virtual Environment**:

   Poetry creates a virtual environment for your project. Activate it with:

   ```shell
   poetry shell
   ```

2. **Start the API Service**:

   ```shell
   python run.py
   ```

3. **Access the API**:

   - The API will be available at `http://localhost:[Project_APP_PORT]`.
   - Explore the API using the Swagger UI at `http://localhost:[Project_APP_PORT]/`.

4. **Making a Call**:

   - Use the `/api/<<resource>>` endpoint to initiate an API Call.

## Documentation

Swagger-based documentation is available at `http://localhost:[Project_APP_PORT]/`. This provides detailed information about all the API endpoints, their expected parameters, and response formats.
