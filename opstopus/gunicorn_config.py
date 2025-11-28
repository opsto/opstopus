"""
Gunicorn configuration file for Opstopus backend.
Configuration is loaded from etc/config.yml
"""
import os
import yaml

# Load configuration from YAML file
# Use absolute path since __file__ may not be available in gunicorn context
CONFIG_PATH = os.path.join("/opstopus", "etc", "config.yml")

with open(CONFIG_PATH, "r") as f:
    app_config = yaml.safe_load(f)

gunicorn_config = app_config.get("gunicorn", {})

# Bind address (must be string)
bind = str(gunicorn_config.get("bind", "0.0.0.0:5080"))

# Worker configuration (must be integers)
workers = int(gunicorn_config.get("workers", 8))
threads = int(gunicorn_config.get("threads", 4))

# Worker class
worker_class = "gthread"

# Timeout configuration
timeout = 120
graceful_timeout = 30
keepalive = 5

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Process naming
proc_name = "opstopus"

# Preload app for better memory usage
preload_app = True

