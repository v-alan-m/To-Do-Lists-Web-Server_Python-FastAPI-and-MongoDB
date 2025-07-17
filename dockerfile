
# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the full application into the image
COPY . /app

# Run without auto-reload
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
