
class DynamicObject(object):
    pass

def desplaza(lat, lon, angulo, distancia):
    punto = DynamicObject()
    punto.latitud = lat
    punto.longitud = lon
    return punto
