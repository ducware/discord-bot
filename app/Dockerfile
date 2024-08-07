FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

# Update pip to the latest version
RUN pip install --upgrade pip

# Install the required packages with increased timeout and use a different mirror
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# Install ffmpeg and libopus
RUN apt-get update && apt-get install -y ffmpeg libopus0 && rm -rf /var/lib/apt/lists/*

COPY . .

# Create symbolic links for data.json if they do not exist
RUN [ ! -e /usr/src/app/name.json ] && ln -s /usr/src/app/data.json /usr/src/app/name.json || true
RUN [ ! -e /usr/src/app/leaderboard.json ] && ln -s /usr/src/app/data.json /usr/src/app/leaderboard.json || true

CMD ["python", "_main_.py"]
