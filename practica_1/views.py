from django.http import HttpResponse
import datetime

def saludo(request):
    documento= """
    <html>
    <body>
    <h1>hola este es nuestra primera pagina en django
    </h1/>
    </body>
    </html>"""

    return HttpResponse(documento)


def inicio(request):
    return HttpResponse("Página de inicio")


def damfecha(request):

    fecha_actual=datetime.datatime.now()
    documento="""
    <html>
    <body>
    <h1>la fecha y hora actuales %s
    </h1/>
    </body>
    </html>""" % fecha_actual

    return  HttpResponse(documento)


def calculaedad(request,agno):
    edadactual=21
    periodo=agno-2023
    edadfutura= edadactual + periodo

    documento="<html><body><h2>En el año %s tendra %s años"%(agno,edadfutura)

    return HttpResponse(documento)



