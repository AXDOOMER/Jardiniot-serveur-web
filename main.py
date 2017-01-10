from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

menu = "Menu: <a href=\"/\">Index</a> | <a href=\"/vision/\">Visionnement</a>"

principale = ("<body><h1>Accueil</h1>" +
    "<h3>Bienvenu sur votre serveur Jardiniot!</h3>" +
    menu +
    "</body>")

visionnement = ("<body><h1>Visionnement du status</h1>" +
    "<h3>Cette page vous permet de visionner le status de votre jardin.</h3>" +
    menu +
    "</body>")

def vision(request):
    return Response(visionnement % request.matchdict)

def index(request):
    return Response(principale % request.matchdict)

if __name__ == '__main__':
    config = Configurator()
    config.add_route('vision', '/vision/')
    config.add_view(vision, route_name='vision')

    config.add_route('index', '/')
    config.add_view(index, route_name='index')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

