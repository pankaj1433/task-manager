FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the dependency files to leverage Docker cache
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry install --no-dev

# Copy the rest of the application code
COPY . /app

# Ensure that the PATH includes the poetry environment
ENV PATH="/root/.local/bin:$PATH"

# Command to run the FastAPI app with Uvicorn
CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
