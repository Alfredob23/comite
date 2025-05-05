from .models import Mensajes

def mensajes_no_leidos(request):
    if request.user.is_authenticated:
        cantidad = Mensajes.objects.filter(leido=False).count()
        return {'mensajes_no_leidos': cantidad}
    return {}