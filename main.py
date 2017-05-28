from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import markdown

style = "<head><link rel=\"stylesheet\" href=\"styles.css\"></head>"

menu = "<hr/>Menu: <a href=\"/\">Index</a> | <a href=\"/vision/\">Visionnement</a><hr/>"

principale = (style + "<body><h1>Accueil</h1>" +
    "<h3>Bienvenu sur votre serveur Jardiniot!</h3>" +
    menu +
    "La communication est établie avec vos jardins. Il y a <b>3</b> jardins détectés. " +
    "</body>")

visionnement = (style + "<body><h1>Visionnement du status</h1>" +
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

status = (style + "<body><h1>Visionnement du status du jardin %(name)s</h1>" +
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

cssfile = open('styles.css', 'r')
css = cssfile.read()

def vision(request):
    return Response(visionnement % request.matchdict)

def jardin(request):
    return Response(status % request.matchdict)

def index(request):
    return Response(principale % request.matchdict)

def test(request):
    return Response(style + mdtest % request.matchdict)

def styles(request):
    return Response(css)

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

    # stupid hack for styles.css, must be specified for every route.
    config.add_route('styles.css', 'styles.css')
    config.add_view(styles, route_name='styles.css')

    config.add_route('md_styles.css', '/test/styles.css')
    config.add_view(styles, route_name='md_styles.css')

    config.add_route('vision_styles.css', '/vision/styles.css')
    config.add_view(styles, route_name='vision_styles.css')

    config.add_route('jardin_styles.css', '/jardin/styles.css')
    config.add_view(styles, route_name='jardin_styles.css')
    # delete and replace every line above until the comment.

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

