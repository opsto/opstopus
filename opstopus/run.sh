#!/bin/bash

# Activate logrotate
cp /opstopus/etc/logrotate /etc/logrotate.d/opstopus
cron    # Start logrotate cron in background

echo "Starting Opstopus Backend..."

# Start gunicorn with configuration file
exec gunicorn -c gunicorn_config.py app:application
