from django.http import HttpResponse
from django.utils.timezone import now, make_aware
import datetime

EXPIRACION = make_aware(datetime.datetime(2025, 3, 24, 20, 41, 59))

def verificar_distintivo(request):
    ahora = now()

    if ahora < EXPIRACION:
        mensaje = "<h1 style='color:green;'>✅ Distintivo válido</h1>"
    else:
        mensaje = "<h1 style='color:red;'>❌ Distintivo no válido. Expirado.</h1>"
    
    return HttpResponse(mensaje) 