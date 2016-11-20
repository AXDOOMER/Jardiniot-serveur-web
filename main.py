from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


#def hello_world(request):
#    return Response('<body><h1>Hello World! %(name)s!</h1></body>' % request.matchdict)

def index(request):
    return Response('<body><h1>Welcome mothafuckeurs!</h1></body>' % request.matchdict)

if __name__ == '__main__':
    config = Configurator()
    #config.add_route('hello', '/hello/{name}')
    #config.add_view(hello_world, route_name='hello')

    config.add_route('index', '/')
    config.add_view(index, route_name='index')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
   
