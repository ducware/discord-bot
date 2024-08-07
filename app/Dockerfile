# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Update pip to the latest version
RUN pip install --upgrade pip

# Install the required packages with increased timeout and use a different mirror
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# Install ffmpeg and libopus
RUN apt-get update && apt-get install -y ffmpeg libopus0 && rm -rf /var/lib/apt/lists/*

# Copy the rest of the application code into the container
COPY . .

# Run the bot
CMD ["python", "_main_.py"]
