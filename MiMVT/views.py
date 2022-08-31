from django.shortcuts import render

from MiMVT.models import Familiar


def datos_padre(request):
    
    padre = Familiar(
        nombre = 'Alberto',
        apellido = 'Diaz',
        nacimiento = "1978-05-25",
        lugar_origen = 'Rio Negro'

    )
    padre.save()
    contexto = {

        'padre':padre

        }

    return render(request, 'padre.html', contexto)

def datos_madre(request):
    
    
    madre = Familiar(
        nombre = 'Patricia',
        apellido = 'Diaz',
        nacimiento = "1980-07-23",
        lugar_origen = 'Capital Federal'

    )
    madre.save()
    contexto2 = {

        'madre':madre

        }

    return render(request, 'madre.html', contexto2)

def datos_tio(request):
    
    
    tio = Familiar(
        nombre = 'Carlos',
        apellido = 'Diaz',
        nacimiento = "1966-12-01",
        lugar_origen = 'Buenos Aires'

    )
    tio.save()
    contexto3 = {

        'tio':tio

        }

    return render(request, 'tio.html', contexto3)
