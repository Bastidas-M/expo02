"""
Módulo para generar reportes de cumplimiento de requisitos de graduación.
"""
import csv
from src.validacion_grado import GraduationValidator
from src.mock_data import get_student_data

def generate_graduation_csv_report(file_path='resultado_graduacion.csv'):
    """
    Genera un reporte CSV con el resultado de la validación de requisitos de graduación
    para los estudiantes listados en el archivo 'estudiantes.txt'.
    
    Args:
        file_path (str, optional): Ruta del archivo CSV a generar.
            Por defecto es 'resultado_graduacion.csv'.
    """
    # Leer los códigos de estudiantes del archivo
    try:
        with open('estudiantes.txt', 'r') as f:
            student_codes = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'estudiantes.txt'")
        return
    
    # Crear el validador
    validator = GraduationValidator()
    
    # Crear el archivo CSV
    with open(file_path, 'w', newline='') as csvfile:
        # Definir los campos del CSV
        fieldnames = [
            'Código', 
            'Nombre', 
            'Matriculado', 
            'Promedio Mínimo', 
            'Paz y Salvo Bienestar', 
            'Derechos de Grado Pagados', 
            'Resultado'
        ]
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Procesar cada estudiante
        for student_code in student_codes:
            # Obtener los resultados de la validación
            graduation_status, requirements = validator.validate_graduation_requirements(student_code)
            
            # Obtener el nombre del estudiante
            student_data = get_student_data(student_code)
            student_name = student_data.get('nombre', 'Desconocido')
            
            # Escribir los resultados en el CSV
            writer.writerow({
                'Código': student_code,
                'Nombre': student_name,
                'Matriculado': 'Sí' if requirements['matriculado'] else 'No',
                'Promedio Mínimo': 'Sí' if requirements['promedio_minimo'] else 'No',
                'Paz y Salvo Bienestar': 'Sí' if requirements['paz_y_salvo_bienestar'] else 'No',
                'Derechos de Grado Pagados': 'Sí' if requirements['derechos_de_grado_pagados'] else 'No',
                'Resultado': 'APROBADO' if graduation_status else 'RECHAZADO'
            })
    
    print(f"Reporte generado exitosamente en '{file_path}'")

if __name__ == "__main__":
    generate_graduation_csv_report()