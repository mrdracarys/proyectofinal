from fpdf import FPDF

class BoletaPDF:
    def __init__(self, boleta):
        self.boleta = boleta

    def generar_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 12)
        pdf.cell(200, 10, txt = f"Boleta para {self.boleta.evento.nombre}", ln = True, align = 'C')
        pdf.cell(200, 10, txt = f"Comprador: {self.boleta.comprador.nombre}", ln = True, align = 'C')
        # Agrega más detalles aquí.
        pdf.output(f"boleta_{self.boleta.id}.pdf")
