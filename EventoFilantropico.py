from Evento import Evento

class EventoFilantropico(Evento):
    def __init__(self, nombre, artistas, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, patrocinadores):
        super().__init__(nombre, artistas, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado)
        self.patrocinadores = patrocinadores

    def calcular_utilidades(self):
        total_aportes = sum([patrocinador['valor'] for patrocinador in self.patrocinadores])
        return total_aportes
