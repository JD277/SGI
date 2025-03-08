import random
import time
from datetime import datetime, timedelta
from dbmanager import DbManager

# Configuración de Firebase
CREDENTIAL_PATH = 'modules/database/estructuras.json'
DATABASE_URL = 'https://estructuras-9be66-default-rtdb.firebaseio.com/'
db_manager = DbManager(CREDENTIAL_PATH, DATABASE_URL)

# Listas de datos venezolanos
CITIES = [
    'Barcelona', 'Puerto La Cruz', 'Lechería', 'Guanta', 'Maracaibo',
    'Valencia', 'Barquisimeto', 'Ciudad Guayana', 'Caracas', 'Mérida',
    'San Cristóbal', 'Maracay', 'Los Teques', 'La Victoria'
]

SERVICES = ['Agua', 'Electricidad','Vialidad','Educacion','Comunicacion','Transporte','Seguridad','Saneamiento']

# Mapeo de tipos de falla por servicio (convertido a diccionario para mejor acceso)
TYPE_OF_FAILURE = {
    'Agua': ['Rotura de Tuberias', 'Falta de suministro' ,'Baja Presion', 'Agua Turbia', 'Contaminacion del Agua'],
    'Salud': ['Falta de Medicamentos', 'Falta de Personal Medico' ,'Equipos Medicos Averiados'],
    'Electricidad': ['Apagon', 'Interrupciones Intermitentes' ,'Baja Tension', 'Sobrecargas'],
    'Vialidad': ['Baches', 'Semaforos Averiados', 'Accidentes Viales'],
    'Educacion': ["Falta de Personal Docente", "Infraestructura Dañada", "Falta de Materiales Educativos"],
    'Comunicacion': ["Cortes de Internet", "Problemas de Telefonia", "Falta de Señal de Television"],
    'Transporte': ["Retrasos en Rutas", "Falta de Unidades", "Problemas de Seguridad"],
    'Seguridad': ["Robos", "Asaltos", "Amenazas", "Problemas de Violencia"],
    "Saneamiento": ["Falta de Recoleccion de Basura", "Contenedores Llenos", "Residuos en la Via Publica"]
}

# Descripciones específicas por tipo de falla
# Descripciones específicas por tipo de falla (completas)
FAILURE_DESCRIPTIONS = {
    # Agua
    'Rotura de Tuberias': 'Fuga masiva en tubería principal afectando distribución en zonas residenciales',
    'Falta de suministro': 'Interrupción completa del suministro de agua en el área afectada',
    'Baja Presion': 'Presión insuficiente en el sistema de distribución de agua',
    'Agua Turbia': 'Agua con alto contenido de sedimentos y partículas visibles',
    'Contaminacion del Agua': 'Presencia de agentes contaminantes detectados en análisis',

    # Electricidad
    'Apagon': 'Interrupción total del suministro eléctrico en el sector',
    'Interrupciones Intermitentes': 'Cortes eléctricos recurrentes cada 2-3 horas',
    'Baja Tension': 'Voltaje por debajo de 110V afectando electrodomésticos',
    'Sobrecargas': 'Frecuentes disparos de breakers por sobrecarga',

    # Vialidad
    'Baches': 'Baches profundos que obstaculizan el tránsito vehicular',
    'Semaforos Averiados': 'Semáforos no funcionales generando caos vial',
    'Accidentes Viales': 'Accidente múltiple bloqueando vías principales',

    # Educación
    'Falta de Personal Docente': 'Aulas sin profesores por ausentismo crónico',
    'Infraestructura Dañada': 'Mobiliario escolar roto y filtraciones en techos',
    'Falta de Materiales Educativos': 'Desabastecimiento de libros y materiales pedagógicos',

    # Comunicación
    'Cortes de Internet': 'Interrupción prolongada del servicio de internet',
    'Problemas de Telefonia': 'Fallas en red móvil y fija en la zona',
    'Falta de Señal de Television': 'Señal de TV abierta inestable o nula',

    # Transporte
    'Retrasos en Rutas': 'Autobuses urbanos con retrasos de 45+ minutos',
    'Falta de Unidades': 'Solo 2 de 10 unidades operativas en la ruta',
    'Problemas de Seguridad': 'Robos frecuentes a usuarios del transporte público',

    # Seguridad
    'Robos': 'Aumento del 70% en robos en el último mes',
    'Asaltos': 'Asaltos violentos en paradas de transporte',
    'Amenazas': 'Amenazas contra comercios locales por grupos delictivos',
    'Problemas de Violencia': 'Peleas callejeras con armas blancas',

    # Saneamiento
    'Falta de Recoleccion de Basura': 'Acumulación de desechos por 5 días sin recolección',
    'Contenedores Llenos': 'Contenedores públicos desbordados',
    'Residuos en la Via Publica': 'Desechos esparcidos por vientos en calles principales'
}

STREETS = [
    'Avenida Bolívar', 'Calle Colombia', 'Avenida Miranda', 'Calle Salazar',
    'Avenida Guzmán', 'Calle Arismendi', 'Avenida Paseo Colón',
    'Calle Las Flores', 'Avenida La Limpia', 'Calle Venezuela'
]

def generate_random_date():
    """Genera fechas aleatorias entre 2020 y 2023"""
    start = datetime(2020, 1, 1)
    end = datetime(2023, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return (start + timedelta(days=random_days)).strftime("%Y-%m-%d %H:%M:%S")

def generate_priority(date_str, description):
    """
    Asigna prioridad basada en antigüedad y palabras clave
    
    Args:
        date_str: Fecha de la falla en formato "%Y-%m-%d %H:%M:%S"
        description: Descripción del reporte
    
    Returns:
        Nivel de prioridad (high/medium/low)
    """
    # Convertir fecha a objeto datetime
    date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    days_old = (datetime.now() - date_obj).days

    # Palabras clave para prioridad
    high_keywords = ['urgente', 'emergencia', 'crítico', 'inmediato']
    medium_keywords = ['importante', 'prioritario', 'necesario']
    
    desc_lower = description.lower()
    
    # Prioridad por antigüedad
    if days_old > 50:
        date_priority = 'high'
    elif days_old > 30:
        date_priority = 'medium'
    else:
        date_priority = 'low'
    
    # Prioridad por palabras clave
    if any(word in desc_lower for word in high_keywords):
        keyword_priority = 'high'
    elif any(word in desc_lower for word in medium_keywords):
        keyword_priority = 'medium'
    else:
        keyword_priority = 'low'
    
    # Combinar prioridades (la más alta prevalece)
    priorities = {'high': 3, 'medium': 2, 'low': 1}
    return max(date_priority, keyword_priority, key=lambda x: priorities[x])

def generate_report():
    """Genera un reporte sintético con datos coherentes"""
    city = random.choice(CITIES)
    service = random.choice(SERVICES)
    
    # Seleccionar tipo de falla según servicio
    failure_type = random.choice(TYPE_OF_FAILURE[service])
    
    # Generar descripción basada en el tipo de falla
    base_description = FAILURE_DESCRIPTIONS.get(
        failure_type,
        f"Problema reportado en el servicio de {service}: {failure_type}"
    )
    
    # Formato de descripción solicitado
    description = f"Tipo de averia: {failure_type} | Descripción: {base_description}"
    
    # Generar fechas
    date_of_failure = generate_random_date()
    date_of_record = generate_random_date()
    
    return {
        "city": city,
        "date_of_record": date_of_record,
        "date_of_failure": date_of_failure,
        "description": description,
        "service": service,
        "street": f"{random.choice(STREETS)} #{random.randint(1, 200)}",
        "priority": generate_priority(date_of_failure, description)
    }

def generate_synthetic_reports(quantity=1000):
    """Genera reportes sintéticos y los guarda en Firebase"""
    for _ in range(quantity):
        try:
            report = generate_report()
            db_manager.write_record(report)
            print(f"Reporte creado: {report['description']} en {report['city']}")
            time.sleep(0.1)  # Evita sobrecarga
        except Exception as e:
            print(f"Error al crear reporte: {e}")

if __name__ == "__main__":
    generate_synthetic_reports(1000)