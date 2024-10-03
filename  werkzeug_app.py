from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    if request.path == '/':
        return Response('<h1>Welcome to My Home Page!</h1>', content_type='text/html')
    elif request.path == '/about':
        return Response('<h1>About This Application</h1><p>This is a simple WSGI app.</p>', content_type='text/html')
    else:
        return Response('<h1>404 Not Found</h1>', status=404, content_type='text/html')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=8080,  # Change to 5555 if you want
        application=application
    )
