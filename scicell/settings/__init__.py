import environ

environ.Env.read_env()
env = environ.Env()

if env('ENVIRON') == 'production':
    from .production import *
else:
    from .development import *
