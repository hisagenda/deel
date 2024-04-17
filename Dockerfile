# Base image
FROM python:3.12-alpine

# Set working directory in the container
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application file into the container
COPY app.py .

# Expose port 5000 for the application to listen on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
