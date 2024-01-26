# gunicorn.conf.py
import multiprocessing

workers = 1  # Start with a conservative number; you can adjust based on performance
timeout = None
