# Use the Ubuntu Desktop as the base image
FROM dorowu/ubuntu-desktop-lxde-vnc

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y requirements.txt

# Copy your game files into the container
COPY . /app/

# Set the working directory
WORKDIR /app

# Start the game when the container runs
CMD ["python3", "mami.py"]
