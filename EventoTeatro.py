from Evento import Evento

class EventoTeatro(Evento):
    def __init__(self, nombre, artistas, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, costo_alquiler):
        super().__init__(nombre, artistas, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado)
        self.costo_alquiler = costo_alquiler

    def to_dict(self):
        data = super().to_dict()
        data['Costo de Alquiler'] = self.costo_alquiler
        return data

    def calcular_utilidades(self, total_boletas_vendidas, precio_boleta):
        ingresos_totales = total_boletas_vendidas * precio_boleta
        tiquetera_retencion = ingresos_totales * 0.07
        utilidades_net = ingresos_totales - tiquetera_retencion - self.costo_alquiler
        return utilidades_net