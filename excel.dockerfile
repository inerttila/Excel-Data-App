# Use an official Python image as the base image
FROM python:3.8-slim-buster

# Install necessary system libraries including tkinter
RUN apt-get update && apt-get install -y \
    python3-tk \
    libgtk-3-0 \
    xfce4 \
    tightvncserver \
    xfonts-base \
    x11-xserver-utils

# Set the VNC password
RUN mkdir -p ~/.vnc && echo "inert" | vncpasswd -f > ~/.vnc/passwd && chmod 600 ~/.vnc/passwd

# Set the display resolution
RUN echo "geometry=1920x1080" >> ~/.vnc/xstartup

# Expose the VNC port
EXPOSE 5902

# Set the environment variable for Xfce
ENV DEBIAN_FRONTEND=noninteractive

# Set the USER environment variable
ENV USER=root

# Create the Xauthority file
RUN touch /root/.Xauthority


# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install your Python dependencies using pip
RUN pip install -r requirements.txt

# Start the VNC server
CMD ["tightvncserver", ":2"]
