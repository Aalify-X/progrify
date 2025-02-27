# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Copy only requirements first to leverage docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data
RUN python -m nltk.downloader punkt wordnet -d /usr/local/share/nltk_data

# Copy the rest of the project files
COPY . .

# Use environment variable for port
ENV PORT=5000

# Expose the port
EXPOSE 5000

# Use gunicorn for production with reduced workers
CMD exec gunicorn --workers 2 --threads 2 --bind 0.0.0.0:${PORT} app:app
