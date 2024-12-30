# Use the official Python image as a base
FROM python:3.10-slim

# Install dependencies for Tkinter and Xvfb
RUN apt-get update && apt-get install -y \
    tk \
    libtk8.6 \
    python3-tk \
    xvfb \
    libx11-dev \
    xorg \
    && pip install --upgrade pip \
    && pip install tkcalendar qrcode openpyxl \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Ensure the Media folder is copied into the container
COPY ./Media /app/Media

# Copy the current directory contents into the container
COPY . /app

    # Use the entrypoint script as the default command
CMD ["python", "excel.pyw"]
