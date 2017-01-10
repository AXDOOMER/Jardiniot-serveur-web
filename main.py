from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

principale = ("<body><h1>Main</h1>" +
    "<b>hello</b>" +
    "</body>")

#def hello_world(request):
#    return Response('<body><h1>Hello World! %(name)s!</h1></body>' % request.matchdict)

def vision(request):
    return Response('<body><h1>Visionnement du status</h1></body>' % request.matchdict)

def index(request):
    return Response(principale % request.matchdict)

if __name__ == '__main__':
    config = Configurator()
    config.add_route('vision', '/vision')
    config.add_view(vision, route_name='vision')

    config.add_route('index', '/')
    config.add_view(index, route_name='index')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

