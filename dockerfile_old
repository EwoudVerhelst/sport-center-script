# Use an official Python runtime as the parent image
# FROM python:3.9-slim-buster
FROM selenium/standalone-chrome

# # Chrome setup
# RUN apt-get update && apt-get install -y \
#     wget \
#     unzip \
#     libglib2.0-0 \
#     libnss3 \
#     libgconf-2-4 \
#     libfontconfig1 \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/* 

# RUN apt-get install -y libxss1 libasound2 libappindicator3-1 libindicator7 libappindicator1 xdg-utils


# # Install Chrome
# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
#     dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# # ChromeDriver setup
# RUN wget https://chromedriver.storage.googleapis.com/91.0.4472.101/chromedriver_linux64.zip && \
#     unzip chromedriver_linux64.zip && \
#     mv chromedriver /usr/bin/chromedriver && \
#     chown root:root /usr/bin/chromedriver && \
#     chmod +x /usr/bin/chromedriver

# # Set environment variable for Chrome (to run it in headless mode)
# ENV DISPLAY=:99

# # Set working directory
# WORKDIR /app

# # Copy requirements.txt and install dependencies
# COPY requirements.txt /app/
# RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the application code to the container
COPY . /app/
