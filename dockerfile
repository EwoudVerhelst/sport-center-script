# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set environment variables
# 1. Set Python to run in unbuffered mode which is recommended when running Python within Docker containers.
# It doesn't allow Python to buffer the outputs. It just prints them directly.
# 2. Ensuring that the Python output is sent straight to terminal (helps in logging)
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/
