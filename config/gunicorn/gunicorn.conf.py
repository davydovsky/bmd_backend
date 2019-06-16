from project.settings.common import LOGGING

logconfig_dict = dict(LOGGING)
bind = ['0.0.0.0:8000']
workers = 4
threads = 2
worker_class = 'sync'
timeout = 180
max_requests = 5000