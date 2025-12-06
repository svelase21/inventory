# Python official image
FROM python:3.11-slim

# Workdir
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all code in the container
COPY . .

# EXPOSE the port when running Uvicorn
EXPOSE 8000

# Running command to start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]