import os

if os.environ['ENVIRON'] == 'production':
    from .production import *
else:
    from .development import *
