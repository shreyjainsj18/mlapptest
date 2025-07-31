# Use an official lightweight Python image as base
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose the port (optional, documentation purpose)
EXPOSE 5000

# Command to start the app server (using gunicorn for production, or flask for simple test)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

# first app is from our app.py file and second app is the Flask app instance
# gunicorn is a WSGI HTTP server for UNIX, which is a good choice for production deployments