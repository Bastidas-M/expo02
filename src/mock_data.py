"""
Módulo para proporcionar datos simulados de estudiantes para las pruebas.
"""

# Diccionario con datos simulados para los estudiantes
# Formateado como {codigo_estudiante: {nombre: str, enrollment: bool, average: float, welfare: bool, payment: bool}}
ESTUDIANTES_DATA = {
    "20210001": {
        "nombre": "Ana Martínez",
        "enrollment": True,
        "average": 4.2,
        "welfare": True,
        "payment": True
    },
    "20210002": {
        "nombre": "Carlos Gutiérrez",
        "enrollment": True,
        "average": 3.8,
        "welfare": True,
        "payment": True
    },
    "20210003": {
        "nombre": "María López",
        "enrollment": True,
        "average": 3.7,
        "welfare": True,
        "payment": True
    },
    "20210004": {
        "nombre": "Juan Rodríguez",
        "enrollment": True,
        "average": 3.2,  # No cumple el promedio mínimo
        "welfare": True,
        "payment": True
    },
    "20210005": {
        "nombre": "Pedro Sánchez",
        "enrollment": True,
        "average": 3.6,
        "welfare": True,
        "payment": False  # No ha pagado los derechos de grado
    }
}

def get_student_data(student_code):
    """
    Obtiene los datos simulados para un estudiante.
    
    Args:
        student_code (str): Código del estudiante.
        
    Returns:
        dict: Datos del estudiante o un diccionario vacío si no existe.
    """
    return ESTUDIANTES_DATA.get(student_code, {})