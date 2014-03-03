
import math

class DynamicObject(object):
    pass
    
TierraRadio = 6371 # kilometros
TierraCircunferencia = TierraRadio * 2 * math.pi;

def desplaza(lat, lon, angulo, distancia):
    punto = DynamicObject()
    punto.latitud = lat
    punto.longitud = lon + math.cos(math.radians(angulo)) * distancia / (TierraCircunferencia / 360)
    return punto
