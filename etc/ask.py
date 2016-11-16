CONFIG = {
    'working_dir': '/home/box/web/ask',
    'environment': {
        'PYTHONPATH': '/home/ilya/anaconda3/envs/test/lib/python3.4/site-packages'
    },
    'args': (
        '--bind=0.0.0.0:8000',
        'ask.wsgi'
    )
}
