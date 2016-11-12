CONFIG = {
    'working_dir': '/home/box/web/ask',
    'environment': {
        'PYTHONPATH': '/usr/lib/python3/dist-packages'
    },
    'args': (
        '--bind=0.0.0.0:8000',
        'ask.wsgi:application'
    )
}
