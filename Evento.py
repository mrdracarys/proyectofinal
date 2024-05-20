# models/evento.py
from abc import ABC, abstractmethod

class Evento(ABC):
    def __init__(self, nombre, artistas, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado):
        self.nombre = nombre
        self.artistas = artistas
        self.fecha = fecha
        self.hora_apertura = hora_apertura
        self.hora_show = hora_show
        self.lugar = lugar
        self.direccion = direccion
        self.ciudad = ciudad
        self.estado = estado

    def to_dict(self):
        return {
            'Nombre': self.nombre,
            'Artistas': self.artistas,
            'Fecha': self.fecha,
            'Hora de Apertura': self.hora_apertura,
            'Hora del Show': self.hora_show,
            'Lugar': self.lugar,
            'Dirección': self.direccion,
            'Ciudad': self.ciudad,
            'Estado': self.estado,
            }

    @abstractmethod
    def calcular_utilidades(self, total_boletas_vendidas):
        pass



