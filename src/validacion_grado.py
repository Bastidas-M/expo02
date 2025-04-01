"""
Módulo para validar los requisitos de graduación de un estudiante.
"""
from src.db_connector import DBConnector

class GraduationValidator:
    """Clase para validar los requisitos de graduación de un estudiante."""
    
    def __init__(self, db_connector=None):
        """
        Inicializa el validador de requisitos de graduación.
        
        Args:
            db_connector (DBConnector, optional): Conector a la base de datos.
                Si no se proporciona, se crea uno nuevo.
        """
        self.db_connector = db_connector or DBConnector()
        self.min_average = 3.5
    
    def check_enrollment(self, student_code):
        """
        Verifica si el estudiante está matriculado.
        
        Args:
            student_code (str): Código del estudiante.
            
        Returns:
            bool: True si el estudiante está matriculado, False en caso contrario.
        """
        return self.db_connector.check_student_enrollment(student_code)
    
    def check_academic_average(self, student_code):
        """
        Verifica si el estudiante cumple con el mínimo promedio requerido.
        
        Args:
            student_code (str): Código del estudiante.
            
        Returns:
            bool: True si el estudiante cumple con el mínimo promedio, False en caso contrario.
        """
        average = self.db_connector.get_student_average(student_code)
        return average >= self.min_average
    
    def check_welfare_status(self, student_code):
        """
        Verifica si el estudiante está a paz y salvo con Bienestar universitario.
        
        Args:
            student_code (str): Código del estudiante.
            
        Returns:
            bool: True si el estudiante está a paz y salvo, False en caso contrario.
        """
        return self.db_connector.check_university_welfare_status(student_code)
    
    def check_payment(self, student_code):
        """
        Verifica si el estudiante ha pagado los derechos de grado.
        
        Args:
            student_code (str): Código del estudiante.
            
        Returns:
            bool: True si el estudiante ha pagado, False en caso contrario.
        """
        return self.db_connector.check_graduation_payment(student_code)
    
    def validate_graduation_requirements(self, student_code):
        """
        Valida si el estudiante cumple con todos los requisitos para graduarse.
        
        Args:
            student_code (str): Código del estudiante.
            
        Returns:
            tuple: (bool, dict) donde el bool indica si cumple con todos los requisitos
                  y el dict contiene el detalle de cada requisito.
        """
        requirements = {
            "matriculado": self.check_enrollment(student_code),
            "promedio_minimo": self.check_academic_average(student_code),
            "paz_y_salvo_bienestar": self.check_welfare_status(student_code),
            "derechos_de_grado_pagados": self.check_payment(student_code)
        }
        
        all_requirements_met = all(requirements.values())
        
        return all_requirements_met, requirements
    
    def generate_graduation_report(self, student_code):
        """
        Genera un informe detallado sobre el cumplimiento de requisitos de graduación.
        
        Args:
            student_code (str): Código del estudiante.
            
        Returns:
            str: Mensaje detallado sobre el cumplimiento de requisitos.
        """
        graduation_status, requirements = self.validate_graduation_requirements(student_code)
        
        if graduation_status:
            message = f"El estudiante con código {student_code} CUMPLE con todos los requisitos para graduarse."
        else:
            message = f"El estudiante con código {student_code} NO CUMPLE con todos los requisitos para graduarse."
        
        message += "\n\nDetalle de requisitos:"
        
        for req_name, req_status in requirements.items():
            status_text = "CUMPLE" if req_status else "NO CUMPLE"
            message += f"\n- {req_name.replace('_', ' ').title()}: {status_text}"
        
        return message


def validate_student_graduation(student_code):
    """
    Función principal que valida si un estudiante cumple con los requisitos para graduarse.
    
    Args:
        student_code (str): Código del estudiante.
        
    Returns:
        str: Mensaje detallado sobre el cumplimiento de requisitos.
    """
    validator = GraduationValidator()
    return validator.generate_graduation_report(student_code)