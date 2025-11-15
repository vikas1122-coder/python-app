# Use official Python image
FROM python:3.11-slim

RUN mkdir ~/application

COPY . ~/application

WORKDIR ~/application

RUN pip install -r requirements.txt

EXPOSE 8000

# Command to run your Python app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
