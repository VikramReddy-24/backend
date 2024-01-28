# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install AWS CLI
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Configure AWS CLI
RUN aws configure set aws_access_key_id AKIAZBJA4O557YOT3PNI \
    && aws configure set aws_secret_access_key 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 \
    && aws configure set region ap-south-1  

# Expose port 8000 for the Django application
EXPOSE 8000

# Run Gunicorn as the entry point for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
