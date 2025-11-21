# Use official Python image
FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .


RUN pip install -r requirements.txt



COPY . .





EXPOSE 8000

# Command to run your Python app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
