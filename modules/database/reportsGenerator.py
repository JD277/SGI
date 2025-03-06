import random
import time
from datetime import datetime, timedelta
from dbmanager import DbManager



# Configuración de Firebase
CREDENTIAL_PATH = 'modules/database/university.json'
DATABASE_URL = 'https://estructuras-9be66-default-rtdb.firebaseio.com/'
db_manager = DbManager(CREDENTIAL_PATH, DATABASE_URL)

# Listas de datos venezolanos
CITIES = [
    'Barcelona', 'Puerto La Cruz', 'Lechería', 'Guanta', 'Maracaibo',
    'Valencia', 'Barquisimeto', 'Ciudad Guayana', 'Caracas', 'Mérida',
    'San Cristóbal', 'Maracay', 'Los Teques', 'La Victoria'
]

SERVICES = ['Agua', 'Electricidad', 'Gas', 'Internet', 'Teléfono']
DESCRIPTIONS = [
    'Fuga de agua en tubería principal',
    'Corte total de electricidad',
    'Baja presión en el suministro de gas',
    'Fibra óptica dañada',
    'Postes eléctricos caídos',
    'Tubería rota en calle principal',
    'Falta de mantenimiento en transformador',
    'Pérdida de señal de internet',
    'Daño en válvula de gas',
    'Cables eléctricos expuestos',
    'Falta de recolección de basura',
    'Baches en la vía pública',
    'Falta de alumbrado público',
    'Tuberías oxidadas',
    'Falta de desagüe pluvial',
    'Daño en estación de bombeo',
    'Falta de mantenimiento en semáforos',
    'Contaminación del agua',
    'Falta de seguridad en la zona',
    'Daño en sistema de cloacas'
]

STREETS = [
    'Avenida Bolívar', 'Calle Colombia', 'Avenida Miranda', 'Calle Salazar',
    'Avenida Guzmán', 'Calle Arismendi', 'Avenida Paseo Colón',
    'Calle Las Flores', 'Avenida La Limpia', 'Calle Venezuela'
]

def generate_random_date():
    """Generate random dates between 2020 y 2023 on UNIX format"""
    start = datetime(2020, 1, 1)
    end = datetime(2023, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return int((start + timedelta(days=random_days)).timestamp())

def generate_priority(date, description):
    """
    Asign the priority by the description and the date
    
    Args:
        date: date of the failure
        description: description of the report
    
    Returns:
        Nivel of the priority (high/medium/low)
    """
    date_obj = datetime.fromtimestamp(date)
    days_old = (datetime.now() - date_obj).days

    if len(description) > 50 and days_old > 365:
        return 'high'
    elif len(description) > 30 and days_old > 180:
        return 'medium'
    else:
        return 'low'

def generate_report():
    """Generates one report"""
    city = random.choice(CITIES)
    service = random.choice(SERVICES)
    description = random.choice(DESCRIPTIONS)
    
    return {
        "city": city,
        "date_of_record": generate_random_date(),
        "date_of_failure": generate_random_date(),
        "description": description,
        "service": service,
        "street": f"{random.choice(STREETS)} #{random.randint(1, 200)}",
        "priority": generate_priority(
            generate_random_date(),
            description
        )
    }

def generate_synthetic_reports(quantity=1000):
    """
    Generates the synthetic reports
    
    Args:
        quantity: the quantity of reports that will be generated
    
    Returns:
        None
    """
    for _ in range(quantity):
        report = generate_report()
        try:
            db_manager.write_record(report)
            print(f"Reporte creado: {report['description']} en {report['city']}")
            time.sleep(0.1)  # Evita sobrecarga de Firebase
        except Exception as e:
            print(f"Error al crear reporte: {e}")

if __name__ == "__main__":
    generate_synthetic_reports(1000)   