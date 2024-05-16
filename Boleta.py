# models/boleta.py
import uuid

class Boleta:
    def __init__(self, evento, comprador, fase_venta, precio):
        self.id = uuid.uuid4()
        self.evento = evento
        self.comprador = comprador
        self.fase_venta = fase_venta
        self.precio = precio
        self.codigo_qr = self.generar_codigo_qr()

    def generar_codigo_qr(self):
        # Implementa la lógica para generar un código QR.
        pass

# models/comprador.py
class Comprador:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
