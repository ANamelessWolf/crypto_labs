"""Define la lista de errores disponibles
"""


class ERROR_MSG:
    #Errores de esteganografía
    ERR_IMG_MISS = "La imagen no existe"
    ERR_BAD_FORMAT = "Actualmente solo se soporta la codificación con Imagenes tipo PNG"
    ERR_IMG_TO_SMALL = "El mensaje es muy largo para la imagen seleccionada"
    ERR_DECODING = "Error al decodificar el mensaje de la imagen seleccionada"
