import os

def simple_app(environ, start_response):
    resp = 'Smart move:\n '
    for i in environ:
        resp += ''.join(f'"{{" {i}:{environ[i]} "}}",\n ')
    start_response("200 OK", [
        ("Content-type", "text/plain"),
        ("Content-length", str(len(resp)))
    ])
    return iter([resp.encode('utf-8')])