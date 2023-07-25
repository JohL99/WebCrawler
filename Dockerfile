# Use the official Python image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /App

# Copy the secrets.py file into the container at /app
COPY App/config.py /App/

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /App/

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /App/

# Set environment variables with default values (optional)
ENV SENDER_EMAIL="Sender@mail.com"
ENV SENDER_PASSWORD="Sender password here"
ENV RECEIVER_EMAIL="Receives@mail.com"

# Use volume mount to allow users to provide their own .env file
VOLUME /App

# Set the command to run your Python application
CMD ["python", "App/main.py"]
