import multiprocessing


bind = "0.0.0.0:5000"  # The host and port where Gunicorn will listen for connections

# Dynamically calculate the number of Gunicorn worker processes based on CPU cores
workers = multiprocessing.cpu_count() * 2 + 1

timeout = 60  # The maximum time in seconds for a worker to handle a request
loglevel = "info"  # The log level for Gunicorn to use
