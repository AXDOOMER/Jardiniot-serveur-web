from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import markdown

style = "<head><link rel=\"stylesheet\" href=\"/static/styles.css\"></head>"

menu = "<hr/>Menu: <a href=\"/\">Index</a> | <a href=\"/vision/\">Visionnement</a><hr/>"

principale = ("<body><h1>Accueil</h1>" +
    "<h3>Bienvenu sur votre serveur Jardiniot!</h3>" +
    menu +
    "La communication est établie avec vos jardins. Il y a <b>3</b> jardins détectés. " +
    "</body>")

visionnement = ("<body><h1>Visionnement du status</h1>" +
    "<h3>Cette page vous permet de visionner le status de vos jardins.</h3>" +
    menu +
    "<table border=\"2\">" +
    "<tr><th>Temperature</th><th>Normale</th></tr>" +
    "<tr><th>Ventillation</th><th>Aucun probleme</th></tr>" +
    "<tr><th>Humidité</th><th>Normale</th></tr>" +
    "<tr><th>Lampe</th><th>Tous en mode nuit</th></tr>" +
    "</table> <br/>" +
    "<h4>Choisir un jardin:</h4>" +
    "<a href=\"/jardin/1\">1</a> | <a href=\"/jardin/2\">2</a> | <a href=\"/jardin/3\">3</a>" +
    "</body>")

status = ("<body><h1>Visionnement du status du jardin %(name)s</h1>" +
    menu +
    "<table border=\"2\">" +
    "<tr><th>Temperature</th><th>22 °C</th></tr>" +
    "<tr><th>Ventillation</th><th>300 RPM</th></tr>" +
    "<tr><th>Humidité</th><th>50 %%</th></tr>" +
    "<tr><th>Lampe</th><th>Activée</th></tr>" +
    "</table> <br/>" +
    "</body>")

mdfile = open('README.md', 'r')
md = mdfile.read()
mdtest = markdown.markdown(md)

#cssfile = open('static/styles.css', 'r')
#css = cssfile.read()

def vision(request):
    return Response(style + visionnement % request.matchdict)

def jardin(request):
    return Response(style + status % request.matchdict)

def index(request):
    return Response(style + principale % request.matchdict)

def test(request):
    return Response(style + mdtest % request.matchdict)

if __name__ == '__main__':
    config = Configurator()
    config.add_route('vision', '/vision/')
    config.add_view(vision, route_name='vision')

    config.add_route('jardin', '/jardin/{name}')
    config.add_view(jardin, route_name='jardin')

    config.add_route('index', '/')
    config.add_view(index, route_name='index')

    config.add_route('test', '/test')
    config.add_view(test, route_name='test')

    config.add_static_view('static', '.', cache_max_age=3600)

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

