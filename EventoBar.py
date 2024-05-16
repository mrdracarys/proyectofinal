from Evento import Evento

class EventoBar(Evento):
    def __init__(self, nombre, artistas, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado):
        super().__init__(nombre, artistas, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado)

    def calcular_utilidades(self, total_boletas_vendidas):
        utilidades_bar = total_boletas_vendidas * 0.2
        utilidades_artista = total_boletas_vendidas * 0.8
        return utilidades_bar, utilidades_artista
