import wsgiref.simple_server

fortune = [
    'Be a generous friend and a fair enemy.',
    'A bargain is something you don\'t need at a price you can\'t resist.',
    'A single conversation with a wise man is better than ten years of study.',
    'All the water in the world can\'t sink a ship unless it gets inside.',
    'Ask a friend to join you on your next voyage.',
    'Back away from individuals who are impulsive.',
    'You\'re working too much! Take a break.',
    'Relaxation is just as essential as work.',
    'Bread today is better than cake tomorrow.',
    'Circumstance does not make the man; it reveals him to himself.',
    'Do not be covered in sadness or be fooled in happiness they both must exist.',
    'Do not fear what you don\'t know.',
    'Do not follow where the path may lead. Go where there is no path...and leave a trail.'
]


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset = utf8')]

    path = environ['PATH_INFO'].split('/')
    if path[1] == 'fortune' and int(path[2]) <= 12:
        start_response('200 OK', headers)
        cookie_number = int(path[2])
        return ['The fortune cookie says... '.encode(), fortune[cookie_number].encode()]
    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()
