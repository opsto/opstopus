FROM python:3.14-trixie
# Debian 13 trixie: https://hub.docker.com/_/python/tags?name=3.14-trixie

# Set working directory
WORKDIR /opstopus

# Set environment variable to avoid pip warnings
ENV PIP_BREAK_SYSTEM_PACKAGES=1
ENV PYTHONIOENCODING=utf-8

# Install system dependencies including PostgreSQL development packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    ssh \
    nano \
    htop \
    unzip \
    wget \
    apt-transport-https \
    lsb-release \
    ca-certificates \
    net-tools \
    fail2ban \
    logrotate

# Install Python dependencies
RUN pip install --upgrade pip==25.3
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ------- above size: 1.66GB -------
# ------- built time: 4 minutes -------


# Set default command
CMD ["/bin/bash"]
