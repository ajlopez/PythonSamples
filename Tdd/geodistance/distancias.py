
import math

class DynamicObject(object):
    pass
    
TierraRadio = 6371 # kilometros
TierraCircunferencia = TierraRadio * 2 * math.pi;

def desplaza(lat, lon, angulo, distancia):
    punto = DynamicObject()
    radianes = math.radians(angulo)
    radio = math.fabs(math.cos(math.radians(lat))) * TierraRadio
    punto.latitud = lat + math.sin(radianes) * distancia / (TierraCircunferencia / 360)
    punto.longitud = lon + math.cos(radianes) * distancia / (radio * 2 * math.pi / 360)
    return punto
