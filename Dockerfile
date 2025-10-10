# Use official Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy dependency file first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Expose the port your app uses (adjust if needed)
EXPOSE 8000

# Command to run your Python app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
