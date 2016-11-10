def hello(env, start_response):
    message = env['QUERY_STRING'].replace('&', '\n')
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [message]