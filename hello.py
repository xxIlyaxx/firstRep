def hello(env, start_response):
    message = env.REQUEST_STRING.split('&')
    start_response('200 OK', [('Content-Type', 'test/plain')])
    return message