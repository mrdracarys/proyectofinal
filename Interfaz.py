# main.py
import streamlit as st
import EventoBar
import EventoTeatro
import EventoFilantropico
import Boleta
import Comprador

def crear_evento_bar():
    st.title('Crear Evento en Bar')
    nombre = st.text_input('Nombre del Evento')
    artistas = st.text_input('Artistas')
    fecha = st.date_input('Fecha del Evento')
    hora_apertura = st.time_input('Hora de Apertura')
    hora_show = st.time_input('Hora del Show')
    lugar = st.text_input('Lugar')
    direccion = st.text_input('Dirección')
    ciudad = st.text_input('Ciudad')
    estado = st.selectbox('Estado', ['Por realizar', 'Realizado', 'Cancelado', 'Aplazado', 'Cerrado'])

    if st.button('Crear Evento'):
        evento = EventoBar(nombre, artistas, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado)
        st.success('Evento creado exitosamente!')

def crear_evento_teatro():
    st.title('Crear Evento en Teatro')
    nombre = st.text_input('Nombre del Evento')
    artistas = st.text_input('Artistas')
    fecha = st.date_input('Fecha del Evento')
    hora_apertura = st.time_input('Hora de Apertura')
    hora_show = st.time_input('Hora del Show')
    lugar = st.text_input('Lugar')
    direccion = st.text_input('Dirección')
    ciudad = st.text_input('Ciudad')
    estado = st.selectbox('Estado', ['Por realizar', 'Realizado', 'Cancelado', 'Aplazado', 'Cerrado'])
    costo_alquiler = st.number_input('Costo de Alquiler', min_value=0)

    if st.button('Crear Evento'):
        evento = EventoTeatro(nombre, artistas, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, costo_alquiler)
        st.success('Evento creado exitosamente!')

def crear_evento_filantropico():
    st.title('Crear Evento Filantrópico')
    nombre = st.text_input('Nombre del Evento')
    artistas = st.text_input('Artistas')
    fecha = st.date_input('Fecha del Evento')
    hora_apertura = st.time_input('Hora de Apertura')
    hora_show = st.time_input('Hora del Show')
    lugar = st.text_input('Lugar')
    direccion = st.text_input('Dirección')
    ciudad = st.text_input('Ciudad')
    estado = st.selectbox('Estado', ['Por realizar', 'Realizado', 'Cancelado', 'Aplazado', 'Cerrado'])
    patrocinadores = st.text_area('Patrocinadores (Nombre y Valor separados por comas)')

    if st.button('Crear Evento'):
        lista_patrocinadores = [{"nombre": p.split(',')[0].strip(), "valor": int(p.split(',')[1].strip())} for p in patrocinadores.split('\n')]
        evento = EventoFilantropico(nombre, artistas, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, lista_patrocinadores)
        st.success('Evento creado exitosamente!')

def main():
    st.sidebar.title('Sistema de Gestión de Eventos de Comedia')
    opciones = ['Crear Evento en Bar', 'Crear Evento en Teatro', 'Crear Evento Filantrópico', 'Ver Eventos', 'Gestionar Boletas', 'Reportes', 'Dashboard']
    eleccion = st.sidebar.selectbox('Seleccione una opción', opciones)

    if eleccion == 'Crear Evento en Bar':
        crear_evento_bar()
    elif eleccion == 'Crear Evento en Teatro':
        crear_evento_teatro()
    elif eleccion == 'Crear Evento Filantrópico':
        crear_evento_filantropico()
    # Añade más
